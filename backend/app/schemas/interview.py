from pydantic import BaseModel


class InterviewQuestionRequest(BaseModel):
    role_title: str
    difficulty: str = "medium"  # easy | medium | hard


class InterviewAnswerRequest(BaseModel):
    question: str
    answer: str
    role_title: str | None = None


class InterviewFeedbackResponse(BaseModel):
    feedback: str
    score: float
    provider_used: str
