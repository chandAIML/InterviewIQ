from pydantic import BaseModel


class VocabularyRequest(BaseModel):
    text: str


class VocabularyResponse(BaseModel):
    suggestions: list[str]
    explanation: str
    provider_used: str
