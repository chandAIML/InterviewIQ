from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here so Alembic / create_all can discover them.
from app.models import user, interview, grammar, vocabulary, resume, progress  # noqa: E402,F401
