from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logging import configure_logging, logger
from app.middleware.logging_middleware import LoggingMiddleware
from app.database.init_db import init_db

from app.api import auth, chat, grammar, vocabulary, interview, resume, dashboard, speech, health

configure_logging()

app = FastAPI(title=settings.APP_NAME, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(grammar.router)
app.include_router(vocabulary.router)
app.include_router(interview.router)
app.include_router(resume.router)
app.include_router(dashboard.router)
app.include_router(speech.router)


@app.on_event("startup")
def on_startup():
    logger.info("Starting %s in %s mode", settings.APP_NAME, settings.ENV)
    try:
        init_db()
    except Exception as exc:  # noqa: BLE001
        logger.warning("Could not initialize database on startup: %s", exc)


@app.get("/")
def root():
    return {"message": "Welcome to the InterviewIQ API. See /docs for the API reference."}
