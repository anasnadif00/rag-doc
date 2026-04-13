"""Conversation memory helpers backed by the async state store."""

from __future__ import annotations

from app.chat.schemas import ConversationMessage
from app.core.config import Settings
from app.tenancy.cache import AsyncStateStore
from app.tenancy.models import SessionPrincipal


class ConversationMemoryService:
    def __init__(self, state_store: AsyncStateStore, settings: Settings) -> None:
        self.state_store = state_store
        self.settings = settings

    def _key(self, principal: SessionPrincipal) -> str:
        return f"chat:memory:{principal.tenant_id}:{principal.user_ref_hash}:{principal.session_id}"

    async def read_history(self, principal: SessionPrincipal) -> list[ConversationMessage]:
        items = await self.state_store.read_list(self._key(principal))
        return [ConversationMessage.model_validate(item) for item in items]

    async def append(self, principal: SessionPrincipal, role: str, content: str) -> None:
        await self.state_store.append_list(
            self._key(principal),
            ConversationMessage(role=role, content=content).model_dump(mode="json"),
            ttl_seconds=self.settings.memory_ttl_seconds,
            trim_to=self.settings.memory_message_limit,
        )

    async def clear(self, principal: SessionPrincipal) -> None:
        await self.state_store.delete(self._key(principal))
