"""Database models."""
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.database import Base


def utc_now():
    return datetime.now(timezone.utc)



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=utc_now)
    last_login = Column(DateTime, default=utc_now)

    # Relationships
    progress_records = relationship("UserLevelProgress", back_populates="user", cascade="all, delete-orphan")
    game_rounds = relationship("GameRound", back_populates="user", cascade="all, delete-orphan")
    words_mastery = relationship("WordMastery", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("UserSettings", back_populates="user", uselist=False, cascade="all, delete-orphan")


class UserLevelProgress(Base):
    __tablename__ = "user_level_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    level = Column(String(10), nullable=False, index=True)  # A1, A2, B1, B2, C1
    difficulty_score = Column(Float, default=0.35)  # 0.0 to 1.0
    total_games = Column(Integer, default=0)
    total_correct = Column(Integer, default=0)
    total_wrong = Column(Integer, default=0)
    average_time = Column(Float, default=0.0)
    accuracy = Column(Float, default=0.0)  # 0 to 100%
    is_unlocked = Column(Boolean, default=True)

    user = relationship("User", back_populates="progress_records")


class GameRound(Base):
    __tablename__ = "game_rounds"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    level = Column(String(10), nullable=False)
    difficulty = Column(Float, default=0.35)
    source_text = Column(Text, nullable=False)  # Uzbek sentence
    target_text = Column(Text, nullable=False)  # English sentence
    words_json = Column(Text, nullable=False)    # JSON list of words & letters
    matrix_letters_json = Column(Text, nullable=False)  # 2D or 1D list of characters in matrix
    grid_size = Column(String(10), default="auto")
    grid_dimension = Column(Integer, default=6)  # e.g., 6 for 6x6
    is_correct = Column(Boolean, default=True)
    response_time = Column(Float, default=0.0)   # Active seconds
    mistake_count = Column(Integer, default=0)
    topic = Column(String(50), default="General")
    content_source = Column(String(30), default="dataset")  # 'ai' or 'dataset'
    created_at = Column(DateTime, default=utc_now)

    user = relationship("User", back_populates="game_rounds")


class WordMastery(Base):
    __tablename__ = "word_mastery"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    word = Column(String(100), nullable=False, index=True)
    translation = Column(String(150), nullable=True)  # Uzbek translation
    wrong_count = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    strength = Column(Integer, default=50)  # 0 to 100
    is_weak = Column(Boolean, default=False)
    next_review = Column(DateTime, default=utc_now)
    last_seen = Column(DateTime, default=utc_now)

    user = relationship("User", back_populates="words_mastery")


class UserSettings(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    current_level = Column(String(10), default="A1")
    preferred_matrix_size = Column(String(10), default="auto")  # auto, 4x4, 5x5, 6x6, 7x7, 8x8
    preferred_topic = Column(String(50), default="General")
    sound_enabled = Column(Boolean, default=True)
    theme = Column(String(20), default="dark")

    user = relationship("User", back_populates="settings")
