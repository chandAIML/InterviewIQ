from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.grammar import GrammarCheckRequest, GrammarCheckResponse
from app.services.grammar_service import check_grammar
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.grammar import GrammarHistory

router = APIRouter(prefix="/api/v1/grammar", tags=["grammar"])


@router.post("/check", response_model=GrammarCheckResponse)
async def check(
    payload: GrammarCheckRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await check_grammar(payload.text)

    db.add(
        GrammarHistory(
            user_id=current_user.id,
            original_text=payload.text,
            corrected_text=result["corrected_text"],
            explanation=result["explanation"],
            score=result["score"],
        )
    )
    db.commit()

    return GrammarCheckResponse(**result)
