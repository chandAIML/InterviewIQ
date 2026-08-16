import re

from app.ai.router import generate_with_fallback
from app.ai.prompt_templates import GRAMMAR_PROMPT


def _parse(raw: str) -> dict:
    corrected = re.search(r"CORRECTED:\s*(.+)", raw)
    explanation = re.search(r"EXPLANATION:\s*(.+)", raw)
    score = re.search(r"SCORE:\s*([\d.]+)", raw)
    return {
        "corrected_text": corrected.group(1).strip() if corrected else raw.strip(),
        "explanation": explanation.group(1).strip() if explanation else "",
        "score": float(score.group(1)) if score else 70.0,
    }


async def check_grammar(text: str) -> dict:
    raw, provider = await generate_with_fallback(GRAMMAR_PROMPT.format(text=text))
    parsed = _parse(raw)
    parsed["provider_used"] = provider
    return parsed
