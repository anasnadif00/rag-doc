"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title="rag-doc API", version="0.1.0")


@app.get("/health", tags=["health"])
def health() -> dict[str, object]:
    return {
        "status": "ok",
        "service": "rag-doc",
        "missing_env": settings.missing_required_env,
    }
