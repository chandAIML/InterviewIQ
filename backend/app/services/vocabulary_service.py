import re

from app.ai.router import generate_with_fallback
from app.ai.prompt_templates import VOCABULARY_PROMPT


def _parse(raw: str) -> dict:
    suggestions = re.search(r"SUGGESTIONS:\s*(.+)", raw)
    explanation = re.search(r"EXPLANATION:\s*(.+)", raw)
    items = [s.strip() for s in suggestions.group(1).split(",")] if suggestions else []
    return {
        "suggestions": items,
        "explanation": explanation.group(1).strip() if explanation else raw.strip(),
    }


async def suggest_vocabulary(text: str) -> dict:
    raw, provider = await generate_with_fallback(VOCABULARY_PROMPT.format(text=text))
    parsed = _parse(raw)
    parsed["provider_used"] = provider
    return parsed
