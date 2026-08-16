from sqlalchemy.orm import Session

from app.core.exceptions import ConflictException, CredentialsException
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User
from app.models.progress import Progress
from app.schemas.user import UserCreate, UserLogin


def register_user(db: Session, payload: UserCreate) -> User:
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise ConflictException("Email already registered")

    user = User(
        full_name=payload.full_name,
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    db.add(Progress(user_id=user.id))
    db.commit()

    return user


def authenticate_user(db: Session, payload: UserLogin) -> str:
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise CredentialsException("Invalid email or password")

    return create_access_token(subject=str(user.id))
