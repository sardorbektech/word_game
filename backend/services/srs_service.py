"""Spaced Repetition System (SRS) and Weak Word Mastery Service."""
from datetime import datetime, timedelta, timezone
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.models import WordMastery
from backend.data.dataset import get_word_translation


class SpacedRepetitionService:
    """Manages word retention, weak word tracking, and review scheduling."""

    # Intervals in days based on consecutive correct streaks
    STREAK_INTERVALS = [1, 3, 7, 14, 30, 60]

    @classmethod
    def record_word_result(
        cls,
        db: Session,
        user_id: int,
        word_text: str,
        is_correct: bool,
        manually_marked: Optional[bool] = None,
        translation: Optional[str] = None
    ) -> WordMastery:
        """Updates word mastery status based on outcome."""
        clean_word = word_text.strip().lower()
        if not clean_word:
            return None

        record = db.query(WordMastery).filter(
            WordMastery.user_id == user_id,
            WordMastery.word == clean_word
        ).first()

        now = datetime.now(timezone.utc)
        uzbek_tr = translation or get_word_translation(clean_word)

        if not record:
            record = WordMastery(
                user_id=user_id,
                word=clean_word,
                translation=uzbek_tr,
                wrong_count=0 if is_correct else 1,
                correct_count=1 if is_correct else 0,
                strength=60 if is_correct else 30,
                is_weak=True if manually_marked or not is_correct else False,
                next_review=now + timedelta(days=1),
                last_seen=now
            )
            db.add(record)
        else:
            record.last_seen = now
            if not record.translation or record.translation == "o'rganilayotgan so'z":
                record.translation = uzbek_tr
            if manually_marked is not None:
                record.is_weak = manually_marked

            if is_correct:
                record.correct_count += 1
                record.strength = min(100, record.strength + 15)

                # Advance next review date
                streak_idx = min(len(cls.STREAK_INTERVALS) - 1, record.correct_count // 2)
                interval_days = cls.STREAK_INTERVALS[streak_idx]
                record.next_review = now + timedelta(days=interval_days)

                # Auto remove weak flag if strength is solid
                if record.strength >= 80 and not manually_marked:
                    record.is_weak = False
            else:
                record.wrong_count += 1
                record.strength = max(10, record.strength - 25)
                # Auto flag as weak after 3 mistakes
                if record.wrong_count >= 3:
                    record.is_weak = True
                # Review soon
                record.next_review = now + timedelta(days=1)

        db.commit()
        db.refresh(record)
        return record

    @classmethod
    def get_weak_words(cls, db: Session, user_id: int, limit: int = 10) -> List[str]:
        """Returns words marked as weak or with low strength."""
        records = db.query(WordMastery).filter(
            WordMastery.user_id == user_id,
            WordMastery.is_weak == True
        ).order_by(WordMastery.strength.asc(), WordMastery.wrong_count.desc()).limit(limit).all()
        return [r.word for r in records]

    @classmethod
    def get_words_due_for_review(cls, db: Session, user_id: int, limit: int = 5) -> List[str]:
        """Returns words scheduled for review now."""
        now = datetime.now(timezone.utc)
        records = db.query(WordMastery).filter(
            WordMastery.user_id == user_id,
            WordMastery.next_review <= now
        ).order_by(WordMastery.strength.asc()).limit(limit).all()
        return [r.word for r in records]
