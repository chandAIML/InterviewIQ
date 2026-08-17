# Architecture

## Overview
InterviewIQ is a full-stack app: a React (Vite) frontend, a FastAPI
backend, a PostgreSQL database, and a multi-provider AI layer with
automatic fallback.

## AI Fallback Flow
```
User -> FastAPI -> AI Router -> Claude
                       |-- if unavailable --> OpenAI
                       |-- if unavailable --> Gemini
                       |-- if unavailable --> Ollama (local)
                       |-- if unavailable --> Offline Knowledge Base
```
Implemented in `backend/app/ai/router.py`. Each provider adapter
(`claude.py`, `openai.py`, `gemini.py`, `ollama.py`) raises
`AIProviderError` on failure or missing credentials so the router can
move to the next one.

## Auth Flow
```
Register -> (optional) Email verification -> Login -> JWT -> Protected APIs
```
JWTs are signed with `SECRET_KEY` (see `app/core/security.py`) and
verified on every protected request via `app/dependencies/auth.py`.

## Layers (backend)
- `api/` — FastAPI routers (HTTP layer only)
- `services/` — business logic, orchestrates AI + DB
- `ai/` — provider adapters + fallback router
- `models/` — SQLAlchemy ORM models
- `schemas/` — Pydantic request/response contracts

## Layers (frontend)
- `pages/` — one screen per route
- `components/` — reusable, mostly presentational
- `context/` + `hooks/` — auth state
- `services/` — typed API calls (axios)
