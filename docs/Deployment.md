# Deployment

## Local (Docker Compose)
```bash
cp .env.example .env   # fill in AI provider keys
docker compose up --build
```
- Frontend: http://localhost:5173
- Backend: http://localhost:8000/docs
- Postgres: localhost:5432

## Manual (no Docker)
**Backend**
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

## Production notes
- Put the frontend build (`npm run build`) behind nginx (see `docker/nginx.conf`).
- Set a strong, unique `SECRET_KEY`.
- Use managed Postgres and enable backups (`scripts/backup_db.sh` for a
  simple local baseline).
- Configure at least one AI provider key; the router degrades
  gracefully but responses are best with Claude/OpenAI/Gemini configured.
