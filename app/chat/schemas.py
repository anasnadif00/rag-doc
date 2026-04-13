"""Schemas for the WebSocket chat runtime."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from app.domain.schemas import KnowledgeCitation, RetrievalOptions, ScreenContext, UserContext


class ConversationMessage(BaseModel):
    role: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ChatTurnRequest(BaseModel):
    type: str = "user_message"
    message: str = Field(..., min_length=1, max_length=2000)
    screen_context: ScreenContext
    retrieval_options: RetrievalOptions | None = None
    user_context: UserContext | None = None


class ChatUsage(BaseModel):
    messages_in: int = 0
    messages_out: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    ws_connects: int = 0


class ChatTurnResponse(BaseModel):
    type: str = "final"
    session_id: str
    answer: str
    steps: list[str]
    citations: list[KnowledgeCitation]
    follow_up_question: str | None
    confidence: float | None
    answer_mode: str
    inference_notice: str | None
    usage: ChatUsage
