"""Rotating refresh-token families backed by the shared state store."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Literal

from app.auth.schemas import RefreshClaims
from app.auth.tokens import TokenValidationError, decode_refresh_token, issue_refresh_token
from app.core.config import Settings
from app.tenancy.cache import AsyncStateStore

RefreshKind = Literal["admin", "chat"]


@dataclass(frozen=True)
class IssuedRefreshToken:
    token: str
    claims: RefreshClaims


class RefreshTokenService:
    def __init__(self, settings: Settings, state_store: AsyncStateStore) -> None:
        self.settings = settings
        self.state_store = state_store

    async def issue_admin(self, *, user_id: str) -> IssuedRefreshToken:
        return await self._issue(
            kind="admin",
            user_id=user_id,
            ttl_seconds=self.settings.admin_refresh_ttl_seconds,
        )

    async def issue_chat(
        self,
        *,
        user_id: str,
        tenant_id: str,
        session_id: str,
        roles: list[str],
        mask_id: str | None,
        mask_permissions: list[str],
        company_code: str | None,
    ) -> IssuedRefreshToken:
        return await self._issue(
            kind="chat",
            user_id=user_id,
            ttl_seconds=self.settings.refresh_ttl_seconds,
            tenant_id=tenant_id,
            session_id=session_id,
            roles=roles,
            mask_id=mask_id,
            mask_permissions=mask_permissions,
            company_code=company_code,
        )

    async def consume(self, token: str, *, expected_kind: RefreshKind) -> RefreshClaims:
        claims = decode_refresh_token(self.settings, token)
        self._ensure_kind(claims, expected_kind)
        if await self.state_store.get_json(self._revoked_key(claims)) is not None:
            raise TokenValidationError("Sessione revocata.")

        family = await self.state_store.pop_json(self._family_key(claims))
        if family is None or family.get("current_jti") != claims.jti:
            await self._mark_family_revoked(claims)
            raise TokenValidationError("Refresh token gia utilizzato o revocato.")
        return claims

    async def rotate(self, claims: RefreshClaims) -> IssuedRefreshToken:
        if await self.state_store.get_json(self._revoked_key(claims)) is not None:
            raise TokenValidationError("Sessione revocata.")

        ttl_seconds = self._ttl_for_kind(claims.kind)
        token, next_claims = issue_refresh_token(
            self.settings,
            kind=claims.kind,
            user_id=claims.sub,
            ttl_seconds=ttl_seconds,
            family_id=claims.fid,
            tenant_id=claims.tid,
            session_id=claims.sid,
            roles=claims.roles,
            mask_id=claims.mask_id,
            mask_permissions=claims.mask_permissions,
            company_code=claims.company_code,
        )
        await self._store_family(next_claims, ttl_seconds=ttl_seconds)

        # A concurrent reuse attempt revokes the whole family while this rotation is in flight.
        if await self.state_store.get_json(self._revoked_key(claims)) is not None:
            await self.state_store.delete(self._family_key(next_claims))
            raise TokenValidationError("Sessione revocata.")
        return IssuedRefreshToken(token=token, claims=next_claims)

    async def revoke(self, token: str | None, *, expected_kind: RefreshKind) -> RefreshClaims | None:
        if not token:
            return None
        try:
            claims = decode_refresh_token(self.settings, token, verify_exp=False)
            self._ensure_kind(claims, expected_kind)
        except TokenValidationError:
            return None

        await self.state_store.delete(self._family_key(claims))
        await self._mark_family_revoked(claims)
        return claims

    async def _issue(
        self,
        *,
        kind: RefreshKind,
        user_id: str,
        ttl_seconds: int,
        tenant_id: str | None = None,
        session_id: str | None = None,
        roles: list[str] | None = None,
        mask_id: str | None = None,
        mask_permissions: list[str] | None = None,
        company_code: str | None = None,
    ) -> IssuedRefreshToken:
        token, claims = issue_refresh_token(
            self.settings,
            kind=kind,
            user_id=user_id,
            ttl_seconds=ttl_seconds,
            tenant_id=tenant_id,
            session_id=session_id,
            roles=roles,
            mask_id=mask_id,
            mask_permissions=mask_permissions,
            company_code=company_code,
        )
        await self._store_family(claims, ttl_seconds=ttl_seconds)
        return IssuedRefreshToken(token=token, claims=claims)

    async def _store_family(self, claims: RefreshClaims, *, ttl_seconds: int) -> None:
        await self.state_store.set_json(
            self._family_key(claims),
            {"current_jti": claims.jti},
            ttl_seconds=ttl_seconds,
        )

    async def _mark_family_revoked(self, claims: RefreshClaims) -> None:
        await self.state_store.delete(self._family_key(claims))
        await self.state_store.set_json(
            self._revoked_key(claims),
            {"revoked": True},
            ttl_seconds=max(1, claims.exp - int(time.time())),
        )

    def _ttl_for_kind(self, kind: RefreshKind) -> int:
        if kind == "admin":
            return self.settings.admin_refresh_ttl_seconds
        return self.settings.refresh_ttl_seconds

    @staticmethod
    def _ensure_kind(claims: RefreshClaims, expected_kind: RefreshKind) -> None:
        if claims.kind != expected_kind:
            raise TokenValidationError("Refresh token non valido per questa sessione.")

    @staticmethod
    def _family_key(claims: RefreshClaims) -> str:
        return f"auth:refresh:{claims.kind}:family:{claims.fid}"

    @staticmethod
    def _revoked_key(claims: RefreshClaims) -> str:
        return f"auth:refresh:{claims.kind}:revoked:{claims.fid}"
