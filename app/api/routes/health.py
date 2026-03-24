"""Health check routes."""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, object]:
    """Return basic service health and missing required environment variables."""
    return {
        "status": "ok",
        "service": "rag-doc",
        "erp_version": settings.erp_version,
        "knowledge_base_path": settings.knowledge_base_path,
        "missing_env": settings.missing_required_env,
    }
