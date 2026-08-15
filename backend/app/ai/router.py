from app.ai import claude, openai, gemini, ollama
from app.core.exceptions import AIProviderError
from app.core.logging import logger

# Fallback chain, in order: Claude -> OpenAI -> Gemini -> Ollama -> Offline KB
_PROVIDERS = [
    ("claude", claude.generate),
    ("openai", openai.generate),
    ("gemini", gemini.generate),
    ("ollama", ollama.generate),
]

_OFFLINE_KB_RESPONSE = (
    "I'm currently running in offline mode because no AI provider is reachable. "
    "Here is some general guidance: structure your answer with a brief summary, "
    "a concrete example, and a short conclusion. Please configure an API key or "
    "start Ollama locally for full AI-powered responses."
)


async def generate_with_fallback(prompt: str, system: str | None = None) -> tuple[str, str]:
    """Try each provider in order. Returns (response_text, provider_name).
    Falls back to a static offline knowledge base response if every provider fails.
    """
    for name, provider_fn in _PROVIDERS:
        try:
            result = await provider_fn(prompt, system)
            if result and result.strip():
                return result, name
        except AIProviderError as exc:
            logger.warning("AI provider '%s' unavailable: %s", name, exc)
            continue

    logger.warning("All AI providers unavailable, falling back to offline knowledge base.")
    return _OFFLINE_KB_RESPONSE, "offline_kb"
