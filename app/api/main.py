"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.api.routes import health_router, ingest_router, query_router


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    app = FastAPI(title="rag-doc API", version="0.1.0")
    app.include_router(health_router)
    app.include_router(ingest_router)
    app.include_router(query_router)
    return app


app = create_app()
