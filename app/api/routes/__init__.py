"""Route registration for the API package."""

from app.api.routes.admin import router as admin_router
from app.api.routes.admin_auth import router as admin_auth_router
from app.api.routes.auth import router as auth_router
from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router
from app.api.routes.ingest import router as ingest_router
from app.api.routes.query import router as query_router

__all__ = [
    "admin_router",
    "admin_auth_router",
    "auth_router",
    "chat_router",
    "health_router",
    "ingest_router",
    "query_router",
]
