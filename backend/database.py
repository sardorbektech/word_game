"""Database connection and session handling."""
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base
from backend.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {},
    pool_pre_ping=True
)

# Tune SQLite for ultra-low memory & CPU footprint (<10MB RAM, fast WAL mode)
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if "sqlite" in settings.DATABASE_URL:
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA synchronous=NORMAL")
        cursor.execute("PRAGMA cache_size=-4000")  # ~4MB memory cache
        cursor.execute("PRAGMA temp_store=MEMORY")
        cursor.execute("PRAGMA mmap_size=30000000")  # 30MB memory mapped I/O
        cursor.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency for obtaining database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
