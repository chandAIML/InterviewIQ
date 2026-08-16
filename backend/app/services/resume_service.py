import re

from app.ai.router import generate_with_fallback
from app.ai.prompt_templates import RESUME_ANALYSIS_PROMPT


def _parse(raw: str) -> dict:
    strengths = re.search(r"STRENGTHS:\s*(.+)", raw)
    improvements = re.search(r"IMPROVEMENTS:\s*(.+)", raw)
    feedback = re.search(r"FEEDBACK:\s*(.+)", raw)
    score = re.search(r"SCORE:\s*([\d.]+)", raw)
    return {
        "strengths": [s.strip() for s in strengths.group(1).split(",")] if strengths else [],
        "improvements": [s.strip() for s in improvements.group(1).split(",")] if improvements else [],
        "feedback": feedback.group(1).strip() if feedback else raw.strip(),
        "score": float(score.group(1)) if score else 60.0,
    }


async def analyze_resume(resume_text: str) -> dict:
    raw, provider = await generate_with_fallback(RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text))
    parsed = _parse(raw)
    parsed["provider_used"] = provider
    return parsed
