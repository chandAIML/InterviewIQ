from app.core.config import settings
from app.core.exceptions import AIProviderError


async def generate(prompt: str, system: str | None = None) -> str:
    if not settings.GEMINI_API_KEY:
        raise AIProviderError("Gemini API key not configured")

    try:
        import google.generativeai as genai

        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction=system or None,
        )
        response = model.generate_content(prompt)
        return response.text or ""
    except Exception as exc:  # noqa: BLE001
        raise AIProviderError(f"Gemini request failed: {exc}") from exc
