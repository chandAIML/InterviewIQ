from pydantic import BaseModel


class DashboardSummary(BaseModel):
    questions_asked: int
    grammar_score: int
    vocabulary_score: int
    interview_score: int
    resume_score: int
    weekly_progress: int
    recent_activity: list[str] = []
