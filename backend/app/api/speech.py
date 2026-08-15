from fastapi import APIRouter, Depends, UploadFile, File

from app.services.speech_service import transcribe_audio, analyze_speech
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/v1/speech", tags=["speech"])


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...), current_user: User = Depends(get_current_user)
):
    audio_bytes = await file.read()
    transcript = await transcribe_audio(audio_bytes)
    result = await analyze_speech(transcript)
    return result
