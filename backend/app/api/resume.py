from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.resume import ResumeAnalysisResponse
from app.services.resume_service import analyze_resume
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.resume import ResumeHistory

router = APIRouter(prefix="/api/v1/resume", tags=["resume"])


@router.post("/analyze", response_model=ResumeAnalysisResponse)
async def analyze(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    raw_bytes = await file.read()
    # NOTE: for a production build, parse PDF/DOCX properly (e.g. pdfplumber, python-docx).
    resume_text = raw_bytes.decode("utf-8", errors="ignore")

    result = await analyze_resume(resume_text)

    db.add(
        ResumeHistory(
            user_id=current_user.id,
            filename=file.filename,
            raw_text=resume_text[:5000],
            feedback=result["feedback"],
            score=result["score"],
        )
    )
    db.commit()

    return ResumeAnalysisResponse(**result)
