"""Shared normalization helpers for KB metadata and retrieval filters."""

from __future__ import annotations

import re
from typing import Any

ERP_VERSION_SEPARATOR_PATTERN = re.compile(r"[\s._-]+")


def normalize_erp_version(value: Any) -> str | None:
    text = str(value or "").strip()
    if not text:
        return None

    normalized = ERP_VERSION_SEPARATOR_PATTERN.sub("", text).casefold()
    return normalized or None


def normalize_erp_version_list(value: Any) -> list[str]:
    if value is None:
        return []

    if isinstance(value, (list, tuple, set)):
        items = value
    else:
        items = str(value).split(",")

    normalized: list[str] = []
    for item in items:
        version = normalize_erp_version(item)
        if version and version not in normalized:
            normalized.append(version)
    return normalized
