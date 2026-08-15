import httpx

from app.core.config import settings
from app.core.exceptions import AIProviderError


async def generate(prompt: str, system: str | None = None) -> str:
    """Call a locally running Ollama instance. Useful as a free, offline-friendly
    fallback before dropping to the static offline knowledge base."""
    full_prompt = f"{system}\n\n{prompt}" if system else prompt

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={"model": "llama3", "prompt": full_prompt, "stream": False},
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "")
    except Exception as exc:  # noqa: BLE001
        raise AIProviderError(f"Ollama request failed: {exc}") from exc
