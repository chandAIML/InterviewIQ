# InterviewIQ

AI-powered interview coaching platform: mock interviews, grammar and
vocabulary correction, resume analysis, voice interviews, and a
progress dashboard — backed by a resilient multi-provider AI layer.

## Stack
- **Frontend:** React + Vite + Tailwind CSS
- **Backend:** FastAPI + SQLAlchemy
- **Database:** PostgreSQL
- **AI:** Claude → OpenAI → Gemini → Ollama → offline knowledge base (automatic fallback)
- **Infra:** Docker Compose, nginx

## Quick start (Docker)
```bash
cp .env.example .env   # add your AI provider keys
docker compose up --build
```
- Frontend: http://localhost:5173
- Backend docs: http://localhost:8000/docs

## Quick start (manual)
```bash
./scripts/install.sh
./scripts/setup_db.sh
# then, in separate terminals:
cd backend && source .venv/bin/activate && uvicorn app.main:app --reload
cd frontend && npm run dev
```

## Features
- AI Interview Coach & Mock Interviews
- Communication / Grammar Checker
- Professional Vocabulary Suggestions
- Resume Analyzer
- Voice Interview & Speech Analysis (starter stub — plug in an STT engine)
- Offline AI fallback so the app degrades gracefully
- Progress Dashboard, Profile, Settings
- Docker-ready, CI/CD-ready, admin-ready architecture

## Project layout
See `docs/Architecture.md` for a full breakdown of the frontend,
backend, database, and AI routing layers.

## Docs
- [API Reference](docs/API.md)
- [Architecture](docs/Architecture.md)
- [Database](docs/Database.md)
- [Deployment](docs/Deployment.md)
- [User Guide](docs/UserGuide.md)

## Tests
```bash
cd backend && pip install -r requirements.txt && pytest ../tests
```

## License
See [LICENSE](LICENSE).
