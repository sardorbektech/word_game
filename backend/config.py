"""Backend configuration module."""
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

    PROJECT_NAME: str = "Adaptive English Sentence Reconstruction Game"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super_secret_adaptive_english_game_key_2026_x")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app_game.db")
    
    # OpenAI config
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY", None)
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    
    # Levels
    VALID_LEVELS: list = ["A1", "A2", "B1", "B2", "C1"]
    DEFAULT_LEVEL: str = "A1"
    
    # Grid sizes supported
    SUPPORTED_GRID_SIZES: list = ["auto", "4x4", "5x5", "6x6", "7x7", "8x8"]


settings = Settings()
