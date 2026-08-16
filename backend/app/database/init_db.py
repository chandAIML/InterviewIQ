from app.database.base import Base
from app.database.session import engine
from app.core.logging import logger


def init_db() -> None:
    """Create all tables. For production use Alembic migrations instead."""
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables ensured (create_all).")
