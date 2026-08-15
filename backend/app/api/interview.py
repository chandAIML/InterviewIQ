import re

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.interview import (
    InterviewQuestionRequest,
    InterviewAnswerRequest,
    InterviewFeedbackResponse,
)
from app.ai.router import generate_with_fallback
from app.ai.prompt_templates import INTERVIEW_QUESTION_PROMPT, INTERVIEW_FEEDBACK_PROMPT
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.interview import InterviewHistory

router = APIRouter(prefix="/api/v1/interview", tags=["interview"])


@router.post("/question")
async def get_question(
    payload: InterviewQuestionRequest, current_user: User = Depends(get_current_user)
):
    prompt = INTERVIEW_QUESTION_PROMPT.format(
        role_title=payload.role_title, difficulty=payload.difficulty
    )
    question, provider = await generate_with_fallback(prompt)
    return {"question": question.strip(), "provider_used": provider}


@router.post("/feedback", response_model=InterviewFeedbackResponse)
async def get_feedback(
    payload: InterviewAnswerRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    prompt = INTERVIEW_FEEDBACK_PROMPT.format(question=payload.question, answer=payload.answer)
    raw, provider = await generate_with_fallback(prompt)

    feedback_match = re.search(r"FEEDBACK:\s*(.+)", raw)
    score_match = re.search(r"SCORE:\s*([\d.]+)", raw)
    feedback = feedback_match.group(1).strip() if feedback_match else raw.strip()
    score = float(score_match.group(1)) if score_match else 65.0

    db.add(
        InterviewHistory(
            user_id=current_user.id,
            role_title=payload.role_title,
            question=payload.question,
            answer=payload.answer,
            feedback=feedback,
            score=score,
        )
    )
    db.commit()

    return InterviewFeedbackResponse(feedback=feedback, score=score, provider_used=provider)
