"""Main FastAPI Application Entry Point."""
import os
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
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
    version="2.1.0",
    description="Adaptive English Sentence Reconstruction Game with Letter Matrix"
)

# GZip compression (reduces payload size by up to 80% on 0.1 CPU)
app.add_middleware(GZipMiddleware, minimum_size=500)

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

# Mount frontend static files with client caching headers
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    class CachedStaticFiles(StaticFiles):
        async def get_response(self, path: str, scope):
            response = await super().get_response(path, scope)
            if response.status_code == 200:
                response.headers["Cache-Control"] = "public, max-age=1800"
            return response

    app.mount("/", CachedStaticFiles(directory=frontend_path, html=True), name="frontend")


@app.get("/api/ping")
def ping():
    """Ultra-fast keep-alive ping for 0.1 CPU server."""
    return {"ping": "pong"}


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "openai_model": settings.OPENAI_MODEL,
        "api_key_configured": bool(settings.OPENAI_API_KEY)
    }
