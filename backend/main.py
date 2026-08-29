"""Main FastAPI Application Entry Point."""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.config import settings
from backend.database import engine, Base
from backend.routers import auth, game, progress, settings as settings_router

from sqlalchemy import text

# Create database tables automatically
Base.metadata.create_all(bind=engine)


def run_migrations():
    """Auto-migrate SQLite tables if new columns are introduced."""
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE word_mastery ADD COLUMN translation VARCHAR(150)"))
            conn.commit()
        except Exception:
            pass
        try:
            conn.execute(text("ALTER TABLE game_rounds ADD COLUMN content_source VARCHAR(30) DEFAULT 'dataset'"))
            conn.commit()
        except Exception:
            pass


run_migrations()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="2.0.0",
    description="Adaptive English Sentence Reconstruction Game with Letter Matrix (Boggle/Word Hunt Swipe Mechanics)"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(auth.router)
app.include_router(game.router)
app.include_router(progress.router)
app.include_router(settings_router.router)

# Mount frontend static files
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "openai_model": settings.OPENAI_MODEL,
        "api_key_configured": bool(settings.OPENAI_API_KEY)
    }
