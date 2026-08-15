from app.core.config import settings
from app.core.exceptions import AIProviderError


async def generate(prompt: str, system: str | None = None) -> str:
    """Call Anthropic's Claude API. Raises AIProviderError on any failure so the
    router can fall back to the next provider in the chain."""
    if not settings.ANTHROPIC_API_KEY:
        raise AIProviderError("Claude API key not configured")

    try:
        import anthropic

        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system or "",
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(block.text for block in message.content if block.type == "text")
    except Exception as exc:  # noqa: BLE001
        raise AIProviderError(f"Claude request failed: {exc}") from exc
