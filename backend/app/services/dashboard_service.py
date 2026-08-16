from sqlalchemy.orm import Session

from app.models.progress import Progress
from app.models.interview import InterviewHistory


def get_dashboard_summary(db: Session, user_id) -> dict:
    progress = db.query(Progress).filter(Progress.user_id == user_id).first()
    recent = (
        db.query(InterviewHistory)
        .filter(InterviewHistory.user_id == user_id)
        .order_by(InterviewHistory.created_at.desc())
        .limit(5)
        .all()
    )

    if not progress:
        return {
            "questions_asked": 0,
            "grammar_score": 0,
            "vocabulary_score": 0,
            "interview_score": 0,
            "resume_score": 0,
            "weekly_progress": 0,
            "recent_activity": [],
        }

    return {
        "questions_asked": progress.questions_asked,
        "grammar_score": progress.grammar_score,
        "vocabulary_score": progress.vocabulary_score,
        "interview_score": progress.interview_score,
        "resume_score": progress.resume_score,
        "weekly_progress": progress.weekly_progress,
        "recent_activity": [r.question for r in recent],
    }
