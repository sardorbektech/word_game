"""Game orchestration API endpoints."""
import json
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User, UserLevelProgress, GameRound, UserSettings
from backend.schemas import (
    GenerateGameRequest,
    GenerateGameResponse,
    SubmitRoundRequest,
    SubmitRoundResponse,
    WordItem
)
from backend.services.auth_service import get_current_user
from backend.services.llm_service import LLMService
from backend.services.grid_engine import GridEmbeddingEngine
from backend.services.difficulty_engine import DifficultyEngine
from backend.services.srs_service import SpacedRepetitionService

router = APIRouter(prefix="/api/game", tags=["game"])


@router.post("/generate", response_model=GenerateGameResponse)
def generate_round(
    req: GenerateGameRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generates a new adaptive round with embedded letter matrix."""
    # 1. Fetch user settings & current level progress
    settings = db.query(UserSettings).filter(UserSettings.user_id == current_user.id).first()
    
    # Strictly prioritize the requested level parameter from frontend click
    raw_level = req.level or (settings.current_level if settings else "A1")
    level = raw_level.strip().upper() if isinstance(raw_level, str) else "A1"
    if level not in ["A1", "A2", "B1", "B2", "C1"]:
        level = "A1"

    if settings and settings.current_level != level:
        settings.current_level = level
        db.commit()

    topic = req.topic or (settings.preferred_topic if settings else "General")
    matrix_size = req.matrix_size or (settings.preferred_matrix_size if settings else "auto")

    progress = db.query(UserLevelProgress).filter(
        UserLevelProgress.user_id == current_user.id,
        UserLevelProgress.level == level
    ).first()

    curr_difficulty = progress.difficulty_score if progress else 0.35

    # 2. Fetch weak words for SRS prompt injection
    weak_words = SpacedRepetitionService.get_weak_words(db, current_user.id, limit=3)
    due_words = SpacedRepetitionService.get_words_due_for_review(db, current_user.id, limit=2)
    priority_words = list(set(weak_words + due_words))

    # 3. Query recently played sentences for this user to avoid repeats
    recent_rounds = db.query(GameRound.target_text).filter(
        GameRound.user_id == current_user.id
    ).order_by(GameRound.created_at.desc()).limit(10).all()
    recent_sentences = [r[0] for r in recent_rounds if r[0]]

    # 4. Request adaptive sentence with anti-repetition filter
    llm_result = LLMService.generate_sentence(
        level=level,
        difficulty=curr_difficulty,
        topic=topic,
        weak_words=priority_words,
        recent_sentences=recent_sentences
    )

    words_list = llm_result["words"]
    if not words_list:
        words_list = ["Hello", "world"]

    # 4. Generate guaranteed embedded grid
    grid, dimension, word_paths = GridEmbeddingEngine.generate_matrix(
        words=words_list,
        level=level,
        requested_size=matrix_size
    )

    # 5. Build structured word items
    structured_words = []
    for idx, w in enumerate(words_list):
        cleaned_word = w.strip().upper()
        structured_words.append(WordItem(
            index=idx,
            word=w,
            letters=[ch for ch in cleaned_word]
        ))

    # 6. Save round to database
    game_round = GameRound(
        user_id=current_user.id,
        level=level,
        difficulty=curr_difficulty,
        source_text=llm_result["source_text"],
        target_text=llm_result["target_text"],
        words_json=json.dumps([item.model_dump() for item in structured_words]),
        matrix_letters_json=json.dumps(grid),
        grid_size=matrix_size,
        grid_dimension=dimension,
        topic=llm_result["topic"],
        content_source=llm_result.get("content_source", "dataset"),
        is_correct=False,
        response_time=0.0,
        mistake_count=0,
        created_at=datetime.now(timezone.utc)
    )
    db.add(game_round)
    db.commit()
    db.refresh(game_round)

    return GenerateGameResponse(
        round_id=game_round.id,
        level=level,
        difficulty=curr_difficulty,
        source_text=llm_result["source_text"],
        target_text=llm_result["target_text"],
        words=structured_words,
        grid=grid,
        grid_dimension=dimension,
        topic=llm_result["topic"],
        content_source=llm_result.get("content_source", "dataset")
    )


@router.post("/submit-round", response_model=SubmitRoundResponse)
def submit_round(
    req: SubmitRoundRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Processes round completion, updates performance stats, SRS, and adaptive difficulty."""
    # 1. Fetch round
    game_round = db.query(GameRound).filter(
        GameRound.id == req.round_id,
        GameRound.user_id == current_user.id
    ).first()

    if not game_round:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Round not found")

    words_data = json.loads(game_round.words_json)
    word_count = len(words_data)
    total_letters = sum(len(w.get("letters", [])) for w in words_data)

    # 2. Calculate performance metrics
    accuracy, expected_time = DifficultyEngine.calculate_round_performance(
        word_count=word_count,
        letter_count=total_letters,
        mistake_count=req.mistake_count,
        active_time_seconds=req.active_time
    )

    # 3. Update level progress
    progress = db.query(UserLevelProgress).filter(
        UserLevelProgress.user_id == current_user.id,
        UserLevelProgress.level == game_round.level
    ).first()

    if not progress:
        progress = UserLevelProgress(
            user_id=current_user.id,
            level=game_round.level,
            difficulty_score=game_round.difficulty
        )
        db.add(progress)

    # Update difficulty
    new_difficulty, difficulty_delta, feedback = DifficultyEngine.update_difficulty(
        current_difficulty=progress.difficulty_score,
        level=game_round.level,
        accuracy=accuracy,
        mistakes=req.mistake_count,
        active_time=req.active_time,
        expected_time=expected_time
    )

    # Update progress aggregates
    progress.total_games += 1
    if req.mistake_count == 0:
        progress.total_correct += 1
    else:
        progress.total_wrong += 1

    # Moving average for accuracy & time
    if progress.total_games == 1:
        progress.accuracy = accuracy
        progress.average_time = req.active_time
    else:
        progress.accuracy = round((progress.accuracy * 0.8) + (accuracy * 0.2), 1)
        progress.average_time = round((progress.average_time * 0.8) + (req.active_time * 0.2), 1)

    progress.difficulty_score = new_difficulty

    # 4. Update GameRound
    game_round.is_correct = req.is_correct
    game_round.mistake_count = req.mistake_count
    game_round.response_time = req.active_time

    # 5. Update SRS for words
    weak_words_updated = []
    for w in words_data:
        word_str = w.get("word", "")
        # If user explicitly marked as learned or made mistakes
        manually_learned = req.learned_words and word_str.lower() in [lw.lower() for lw in req.learned_words]
        is_word_correct = (req.mistake_count == 0) and not manually_learned
        record = SpacedRepetitionService.record_word_result(
            db=db,
            user_id=current_user.id,
            word_text=word_str,
            is_correct=is_word_correct,
            manually_marked=True if manually_learned else None
        )
        if record and record.is_weak:
            weak_words_updated.append(record.word)

    db.commit()

    return SubmitRoundResponse(
        is_success=True,
        accuracy=accuracy,
        mistakes=req.mistake_count,
        active_time=req.active_time,
        new_difficulty=new_difficulty,
        difficulty_delta=difficulty_delta,
        level=game_round.level,
        weak_words_updated=list(set(weak_words_updated)),
        message=feedback
    )
