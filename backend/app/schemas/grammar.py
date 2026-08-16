from pydantic import BaseModel


class GrammarCheckRequest(BaseModel):
    text: str


class GrammarCheckResponse(BaseModel):
    corrected_text: str
    explanation: str
    score: float
    provider_used: str
