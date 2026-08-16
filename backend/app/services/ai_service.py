from app.ai.router import generate_with_fallback
from app.ai.prompt_templates import CHAT_COACH_SYSTEM_PROMPT


async def ask_coach(message: str, context: str | None = None) -> tuple[str, str]:
    prompt = message if not context else f"Context: {context}\n\nUser: {message}"
    return await generate_with_fallback(prompt, system=CHAT_COACH_SYSTEM_PROMPT)
