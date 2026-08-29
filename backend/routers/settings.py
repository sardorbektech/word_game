"""User Settings API endpoints."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User, UserSettings
from backend.schemas import UserSettingsResponse, UpdateSettingsRequest
from backend.services.auth_service import get_current_user
from backend.config import settings

router = APIRouter(prefix="/api/settings", tags=["settings"])


@router.get("", response_model=UserSettingsResponse)
def get_user_settings(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retrieves user game and interface settings."""
    user_settings = db.query(UserSettings).filter(UserSettings.user_id == current_user.id).first()
    if not user_settings:
        user_settings = UserSettings(
            user_id=current_user.id,
            current_level="A1",
            preferred_matrix_size="auto",
            preferred_topic="General",
            sound_enabled=True,
            theme="dark"
        )
        db.add(user_settings)
        db.commit()
        db.refresh(user_settings)

    return UserSettingsResponse.model_validate(user_settings)


@router.put("", response_model=UserSettingsResponse)
def update_user_settings(
    req: UpdateSettingsRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Updates user game and interface settings."""
    user_settings = db.query(UserSettings).filter(UserSettings.user_id == current_user.id).first()
    if not user_settings:
        user_settings = UserSettings(user_id=current_user.id)
        db.add(user_settings)

    if req.current_level is not None:
        if req.current_level.upper() in settings.VALID_LEVELS:
            user_settings.current_level = req.current_level.upper()

    if req.preferred_matrix_size is not None:
        if req.preferred_matrix_size.lower() in settings.SUPPORTED_GRID_SIZES:
            user_settings.preferred_matrix_size = req.preferred_matrix_size.lower()

    if req.preferred_topic is not None:
        user_settings.preferred_topic = req.preferred_topic

    if req.sound_enabled is not None:
        user_settings.sound_enabled = req.sound_enabled

    if req.theme is not None:
        user_settings.theme = req.theme

    db.commit()
    db.refresh(user_settings)
    return UserSettingsResponse.model_validate(user_settings)
