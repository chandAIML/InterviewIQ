from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    feedback: str
    score: float
    strengths: list[str]
    improvements: list[str]
    provider_used: str
