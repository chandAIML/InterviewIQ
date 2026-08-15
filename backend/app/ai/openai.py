from app.core.config import settings
from app.core.exceptions import AIProviderError


async def generate(prompt: str, system: str | None = None) -> str:
    if not settings.OPENAI_API_KEY:
        raise AIProviderError("OpenAI API key not configured")

    try:
        from openai import OpenAI

        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=1024,
        )
        return response.choices[0].message.content or ""
    except Exception as exc:  # noqa: BLE001
        raise AIProviderError(f"OpenAI request failed: {exc}") from exc
