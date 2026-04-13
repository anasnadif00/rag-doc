"""Tenant-scoped security helpers."""

from __future__ import annotations

import hashlib
import hmac


def hash_user_reference(tenant_id: str, user_id: str, salt: str) -> str:
    payload = f"{tenant_id}:{user_id}".encode("utf-8")
    key = salt.encode("utf-8")
    return hmac.new(key, payload, hashlib.sha256).hexdigest()
