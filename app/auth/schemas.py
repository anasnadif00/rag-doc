"""Schemas for bootstrap auth and runtime tokens."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class BootstrapRequest(BaseModel):
    bootstrap_token: str = Field(..., min_length=1)


class BootstrapClaims(BaseModel):
    iss: str
    aud: str
    tid: str
    sub: str
    jti: str
    exp: int
    iat: int
    roles: list[str] = Field(default_factory=list)
    mask_id: str | None = None
    mask_permissions: list[str] = Field(default_factory=list)
    company_code: str | None = None


class BootstrapResponse(BaseModel):
    session_id: str
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    tenant_id: str
    tenant_code: str
    display_name: str


class SessionClaims(BaseModel):
    iss: str
    aud: str
    tid: str
    sub: str
    sid: str
    exp: int
    iat: int
    roles: list[str] = Field(default_factory=list)
    mask_id: str | None = None
    mask_permissions: list[str] = Field(default_factory=list)
    company_code: str | None = None


class AdminLoginRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=100)
    password: str = Field(..., min_length=1, max_length=255)


class AdminSessionClaims(BaseModel):
    iss: str
    aud: str
    sub: str
    usr: str
    name: str
    exp: int
    iat: int


class AdminSessionResponse(BaseModel):
    username: str
    display_name: str
    expires_in: int


class AdminSessionInfoResponse(BaseModel):
    username: str
    display_name: str


class WSTicketResponse(BaseModel):
    ticket: str
    expires_in: int


class WSTicketPayload(BaseModel):
    ticket: str
    session_id: str
    tenant_id: str
    tenant_code: str
    user_id: str
    user_ref_hash: str
    roles: list[str] = Field(default_factory=list)
    mask_id: str | None = None
    mask_permissions: list[str] = Field(default_factory=list)
    company_code: str | None = None
    expires_at: datetime


class WebChatSessionResponse(BaseModel):
    session_id: str
    display_name: str
    expires_in: int
