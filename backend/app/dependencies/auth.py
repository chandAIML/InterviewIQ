from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.core.exceptions import CredentialsException
from app.core.security import decode_access_token
from app.database.session import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise CredentialsException()
    except JWTError as exc:
        raise CredentialsException() from exc

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise CredentialsException()
    return user
