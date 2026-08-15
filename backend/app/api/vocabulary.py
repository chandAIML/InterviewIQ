from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.vocabulary import VocabularyRequest, VocabularyResponse
from app.services.vocabulary_service import suggest_vocabulary
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.vocabulary import VocabularyHistory

router = APIRouter(prefix="/api/v1/vocabulary", tags=["vocabulary"])


@router.post("/suggest", response_model=VocabularyResponse)
async def suggest(
    payload: VocabularyRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await suggest_vocabulary(payload.text)

    db.add(
        VocabularyHistory(
            user_id=current_user.id,
            word_or_phrase=payload.text,
            suggestion=", ".join(result["suggestions"]),
            context=result["explanation"],
        )
    )
    db.commit()

    return VocabularyResponse(**result)
