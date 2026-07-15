"""Schemas for provider admin control-plane APIs."""

from __future__ import annotations

from datetime import date, datetime

from pydantic import BaseModel, Field, field_validator


class ModelSettingsUpdateRequest(BaseModel):
    generation_model: str = Field(..., min_length=1, max_length=255)
    rerank_model: str = Field(..., min_length=1, max_length=255)

    @field_validator("generation_model", "rerank_model")
    @classmethod
    def validate_model_id(cls, value: str) -> str:
        model_id = value.strip()
        if not model_id or any(character.isspace() for character in model_id):
            raise ValueError("L'identificativo del modello non puo contenere spazi.")
        return model_id


class ModelSettingsResponse(BaseModel):
    generation_model: str
    rerank_model: str
    available_models: list[str]
    persisted: bool


class TenantLicensePayload(BaseModel):
    status: str = "active"
    daily_message_limit: int = Field(default=500, ge=1)
    daily_token_limit: int = Field(default=500000, ge=1)
    burst_rps_limit: int = Field(default=5, ge=1)
    concurrent_sessions_limit: int = Field(default=10, ge=1)
    overlay_kb_enabled: bool = False
    erp_tools_enabled: bool = False


class TenantCreateRequest(BaseModel):
    tenant_code: str = Field(..., min_length=2, max_length=100)
    display_name: str = Field(..., min_length=2, max_length=255)
    issuer: str = Field(..., min_length=3, max_length=255)
    allowed_origins: list[str] = Field(default_factory=list)
    license_tier: str = "standard"
    overlay_collection: str | None = None
    public_key_pem: str | None = None
    public_key_kid: str | None = None
    license: TenantLicensePayload | None = None


class TenantUpdateRequest(BaseModel):
    display_name: str | None = Field(default=None, min_length=2, max_length=255)
    status: str | None = None
    allowed_origins: list[str] | None = None
    license_tier: str | None = None
    overlay_collection: str | None = None


class TenantLicenseUpdateRequest(BaseModel):
    status: str | None = None
    daily_message_limit: int | None = Field(default=None, ge=1)
    daily_token_limit: int | None = Field(default=None, ge=1)
    burst_rps_limit: int | None = Field(default=None, ge=1)
    concurrent_sessions_limit: int | None = Field(default=None, ge=1)
    overlay_kb_enabled: bool | None = None
    erp_tools_enabled: bool | None = None


class TenantKeyRotateRequest(BaseModel):
    public_key_pem: str = Field(..., min_length=1)
    kid: str | None = None
    algorithm: str = "RS256"


class TenantLicenseResponse(BaseModel):
    status: str
    daily_message_limit: int
    daily_token_limit: int
    burst_rps_limit: int
    concurrent_sessions_limit: int
    overlay_kb_enabled: bool
    erp_tools_enabled: bool


class TenantResponse(BaseModel):
    id: str
    tenant_code: str
    display_name: str
    issuer: str
    status: str
    license_tier: str
    allowed_origins: list[str]
    overlay_collection: str | None
    active_kid: str | None = None
    license: TenantLicenseResponse


class TenantUsageDay(BaseModel):
    usage_date: date
    messages_in: int
    messages_out: int
    prompt_tokens: int
    completion_tokens: int
    ws_connects: int


class TenantUserCreateRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=100)
    display_name: str = Field(..., min_length=1, max_length=255)
    expires_at: datetime | None = None

    @field_validator("username", "display_name")
    @classmethod
    def validate_not_blank(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("Il campo non puo essere vuoto.")
        return cleaned_value


class TenantUserResponse(BaseModel):
    id: str
    tenant_id: str
    username: str
    display_name: str
    status: str
    rotated_at: datetime | None = None
    expires_at: datetime | None = None
    created_at: datetime


class TenantUserSecretResponse(BaseModel):
    user: TenantUserResponse
    temporary_password: str
