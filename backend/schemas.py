"""Pydantic schemas for request and response validation."""
from typing import List, Optional, Any
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Auth schemas
class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    password: str = Field(..., min_length=4, max_length=100)


class UserLoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str
    current_level: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    current_level: str
    created_at: datetime


# Game schemas
class WordItem(BaseModel):
    index: int
    word: str
    letters: List[str]


class GenerateGameRequest(BaseModel):
    level: Optional[str] = None
    topic: Optional[str] = None
    matrix_size: Optional[str] = None


class GenerateGameResponse(BaseModel):
    round_id: int
    level: str
    difficulty: float
    source_text: str
    target_text: str
    words: List[WordItem]
    grid: List[List[str]]
    grid_dimension: int
    topic: str
    content_source: str = "dataset"  # 'ai' or 'dataset'


class SubmitRoundRequest(BaseModel):
    round_id: int
    active_time: float
    mistake_count: int
    is_correct: bool = True
    learned_words: Optional[List[str]] = []


class SubmitRoundResponse(BaseModel):
    is_success: bool
    accuracy: float
    mistakes: int
    active_time: float
    new_difficulty: float
    difficulty_delta: float
    level: str
    weak_words_updated: List[str]
    message: str


# Progress schemas
class LevelProgressItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    level: str
    difficulty_score: float
    total_games: int
    total_correct: int
    total_wrong: int
    accuracy: float
    average_time: float
    is_unlocked: bool


class ProgressSummaryResponse(BaseModel):
    current_level: str
    levels: List[LevelProgressItem]
    total_weak_words: int
    total_games_played: int


# Word Mastery
class WordMasteryItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    word: str
    translation: Optional[str] = None
    wrong_count: int
    correct_count: int
    strength: int
    is_weak: bool
    last_seen: datetime


# Settings schemas
class UserSettingsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    current_level: str
    preferred_matrix_size: str
    preferred_topic: str
    sound_enabled: bool
    theme: str


class UpdateSettingsRequest(BaseModel):
    current_level: Optional[str] = None
    preferred_matrix_size: Optional[str] = None
    preferred_topic: Optional[str] = None
    sound_enabled: Optional[bool] = None
    theme: Optional[str] = None
