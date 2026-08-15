from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_service import ask_coach
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/v1/chat", tags=["chat"])


@router.post("/", response_model=ChatResponse)
async def chat(payload: ChatRequest, current_user: User = Depends(get_current_user)):
    reply, provider = await ask_coach(payload.message, payload.context)
    return ChatResponse(reply=reply, provider_used=provider)
