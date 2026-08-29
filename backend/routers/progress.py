"""Progress and Word Mastery API endpoints."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User, UserLevelProgress, WordMastery, UserSettings
from backend.schemas import (
    ProgressSummaryResponse,
    LevelProgressItem,
    WordMasteryItem
)
from backend.services.auth_service import get_current_user
from backend.services.srs_service import SpacedRepetitionService

router = APIRouter(prefix="/api/progress", tags=["progress"])


@router.get("/summary", response_model=ProgressSummaryResponse)
def get_progress_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retrieves full multi-level progress summary."""
    user_settings = db.query(UserSettings).filter(UserSettings.user_id == current_user.id).first()
    curr_lvl = user_settings.current_level if user_settings else "A1"

    records = db.query(UserLevelProgress).filter(
        UserLevelProgress.user_id == current_user.id
    ).all()

    # Map to schema
    items = []
    total_games = 0
    for r in records:
        total_games += r.total_games
        items.append(LevelProgressItem.model_validate(r))

    weak_words_count = db.query(WordMastery).filter(
        WordMastery.user_id == current_user.id,
        WordMastery.is_weak == True
    ).count()

    return ProgressSummaryResponse(
        current_level=curr_lvl,
        levels=items,
        total_weak_words=weak_words_count,
        total_games_played=total_games
    )


@router.get("/weak-words", response_model=List[WordMasteryItem])
def get_weak_words_list(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retrieves all active weak words."""
    words = db.query(WordMastery).filter(
        WordMastery.user_id == current_user.id,
        WordMastery.is_weak == True
    ).order_by(WordMastery.strength.asc()).all()
    return [WordMasteryItem.model_validate(w) for w in words]


@router.post("/words/{word}/mark")
def mark_word_weak(
    word: str,
    translation: str = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Manually marks a word for reinforcement."""
    record = SpacedRepetitionService.record_word_result(
        db=db,
        user_id=current_user.id,
        word_text=word,
        is_correct=False,
        manually_marked=True,
        translation=translation
    )
    return {"status": "success", "word": record.word, "translation": record.translation, "is_weak": record.is_weak}


@router.delete("/words/{word}/mark")
def unmark_word_weak(
    word: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Manually unmarks a weak word."""
    record = db.query(WordMastery).filter(
        WordMastery.user_id == current_user.id,
        WordMastery.word == word.strip().lower()
    ).first()
    if record:
        record.is_weak = False
        record.strength = max(record.strength, 80)
        db.commit()
    return {"status": "success", "word": word}
