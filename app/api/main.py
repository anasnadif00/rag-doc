"""FastAPI application entrypoint."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import (
    admin_router,
    admin_auth_router,
    auth_router,
    chat_router,
    health_router,
    ingest_router,
    query_router,
)
from app.persistence.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    app = FastAPI(title="rag-doc API", version="0.1.0", lifespan=lifespan)
    app.include_router(health_router)
    app.include_router(ingest_router)
    app.include_router(query_router)
    app.include_router(admin_auth_router)
    app.include_router(auth_router)
    app.include_router(admin_router)
    app.include_router(chat_router)
    return app

app = create_app()
