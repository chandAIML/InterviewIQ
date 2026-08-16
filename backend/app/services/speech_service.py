"""Speech analysis service.

This is a runnable starter stub. Wire up a real speech-to-text engine
(e.g. Whisper, Google Speech-to-Text) by replacing `transcribe_audio`.
"""


async def transcribe_audio(audio_bytes: bytes) -> str:
    # TODO: integrate a real STT engine. Returning a placeholder for now
    # so the API contract works end-to-end during development.
    return "[transcription placeholder - integrate a speech-to-text engine]"


async def analyze_speech(transcript: str) -> dict:
    word_count = len(transcript.split())
    return {
        "transcript": transcript,
        "word_count": word_count,
        "pace_feedback": "Looks reasonable" if word_count > 5 else "Answer seems short",
    }
