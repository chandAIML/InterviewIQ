# Database

PostgreSQL, managed via `database/schema.sql` (or SQLAlchemy
`create_all` in dev — see `backend/app/database/init_db.py`).

## Tables
- **users** — accounts and credentials
- **interview_history** — mock interview Q&A, feedback, scores
- **grammar_history** — grammar check submissions and corrections
- **vocabulary_history** — vocabulary suggestion requests
- **resume_history** — uploaded resumes and analysis
- **progress** — per-user rollup scores shown on the dashboard
- **achievements** — unlocked badges
- **settings** — per-user preferences (theme, notifications, AI provider)
- **notifications** — in-app notifications

## Setup
```bash
createdb interviewiq
psql -U postgres -d interviewiq -f database/schema.sql
psql -U postgres -d interviewiq -f database/seed.sql
psql -U postgres -d interviewiq -f database/sample_data.sql   # optional demo data
```

## Migrations
`database/migrations/` is reserved for Alembic migrations once the
schema stabilizes. For now, `schema.sql` is the source of truth and
`Base.metadata.create_all()` keeps local dev in sync automatically.
