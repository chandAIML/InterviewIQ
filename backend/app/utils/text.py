import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def truncate(text: str, max_len: int = 280) -> str:
    return text if len(text) <= max_len else text[: max_len - 1].rstrip() + "…"
