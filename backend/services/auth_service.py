"""Authentication and JWT token helper services using direct bcrypt."""
from datetime import datetime, timedelta, timezone
from typing import Optional
import bcrypt
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from backend.config import settings
from backend.database import get_db
from backend.models import User, UserSettings, UserLevelProgress

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


class AuthService:
    """Handles password hashing, token encoding, and authentication dependencies."""

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verifies plaintext password against bcrypt hash."""
        try:
            password_bytes = plain_password.encode('utf-8')[:72]
            hashed_bytes = hashed_password.encode('utf-8')
            return bcrypt.checkpw(password_bytes, hashed_bytes)
        except Exception:
            return False

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Hashes plaintext password using bcrypt."""
        password_bytes = password.encode('utf-8')[:72]
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode('utf-8')

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def init_user_defaults(db: Session, user: User):
        """Initializes default settings and level progress records for a new user."""
        # 1. User settings
        user_settings = UserSettings(
            user_id=user.id,
            current_level="A1",
            preferred_matrix_size="auto",
            preferred_topic="General",
            sound_enabled=True,
            theme="dark"
        )
        db.add(user_settings)

        # 2. Progress records for each CEFR level
        for lvl in settings.VALID_LEVELS:
            baseline_diff = 0.20 if lvl == "A1" else (0.35 if lvl == "A2" else (0.50 if lvl == "B1" else (0.65 if lvl == "B2" else 0.80)))
            progress = UserLevelProgress(
                user_id=user.id,
                level=lvl,
                difficulty_score=baseline_diff,
                total_games=0,
                total_correct=0,
                total_wrong=0,
                average_time=0.0,
                accuracy=0.0,
                is_unlocked=True
            )
            db.add(progress)

        db.commit()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """Dependency to retrieve currently authenticated user from Bearer token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user
