"""Authentication API endpoints."""
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User, UserSettings
from backend.schemas import UserRegisterRequest, UserLoginRequest, TokenResponse, UserResponse
from backend.services.auth_service import AuthService, get_current_user

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse)
def register(req: UserRegisterRequest, db: Session = Depends(get_db)):
    """Registers a new user account."""
    existing_user = db.query(User).filter(User.username == req.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ushbu foydalanuvchi nomi band. Boshqa nom tanlang."
        )

    now = datetime.now(timezone.utc)
    hashed = AuthService.get_password_hash(req.password)
    new_user = User(
        username=req.username,
        hashed_password=hashed,
        created_at=now,
        last_login=now
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Initialize level progress and default settings
    AuthService.init_user_defaults(db, new_user)

    # Create access token
    access_token = AuthService.create_access_token(data={"sub": new_user.username})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        username=new_user.username,
        current_level="A1"
    )


@router.post("/login", response_model=TokenResponse)
def login(req: UserLoginRequest, db: Session = Depends(get_db)):
    """Logs in an existing user."""
    user = db.query(User).filter(User.username == req.username).first()
    if not user or not AuthService.verify_password(req.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Foydalanuvchi nomi yoki parol noto'g'ri."
        )

    user.last_login = datetime.now(timezone.utc)
    db.commit()

    # Get user's current level
    user_settings = db.query(UserSettings).filter(UserSettings.user_id == user.id).first()
    curr_lvl = user_settings.current_level if user_settings else "A1"

    access_token = AuthService.create_access_token(data={"sub": user.username})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        username=user.username,
        current_level=curr_lvl
    )


@router.get("/me", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Returns profile information for the authenticated user."""
    user_settings = db.query(UserSettings).filter(UserSettings.user_id == current_user.id).first()
    curr_lvl = user_settings.current_level if user_settings else "A1"
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        current_level=curr_lvl,
        created_at=current_user.created_at
    )
