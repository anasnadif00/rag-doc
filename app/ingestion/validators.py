"""Validation helpers for the ERP knowledge base contract."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from app.core.normalization import normalize_erp_version_list
from app.domain.schemas import DocType, KBValidationError, ReviewStatus

SUPPORTED_DOC_KINDS = {"how_to", "troubleshooting", "reference", "faq", "overview"}
LEGACY_DOC_KIND_MAPPING = {
    "manual": "how_to",
    "manuals": "how_to",
    "sop": "how_to",
    "sops": "how_to",
    "faq": "troubleshooting",
    "faqs": "troubleshooting",
    "field_reference": "reference",
    "field-references": "reference",
    "error_reference": "troubleshooting",
    "error-references": "troubleshooting",
}
REQUIRED_FIELDS = (
    "title",
    "doc_kind",
    "domain",
    "feature",
    "keywords",
    "task_tags",
    "erp_versions",
    "role_scope",
    "review_status",
)
REVIEW_STATUSES = {"draft", "review", "approved", "deprecated"}


def normalize_doc_kind(value: Any, fallback: str = "overview") -> DocType:
    normalized = str(value or fallback).strip().lower().replace("-", "_")
    mapped = LEGACY_DOC_KIND_MAPPING.get(normalized, normalized)
    if mapped not in SUPPORTED_DOC_KINDS:
        mapped = fallback
    return mapped  # type: ignore[return-value]


def normalize_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [item.strip() for item in str(value).split(",") if item.strip()]


# gets the metadata from the markdown file, the payload and list of errors if found
def parse_yaml_front_matter(path: Path, raw_text: str) -> tuple[dict[str, Any], str, list[KBValidationError]]:
    if path.suffix.lower() != ".md":
        return {}, raw_text.strip(), []

    lines = raw_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, raw_text.strip(), [KBValidationError(kb_path=path.as_posix(), message="Missing YAML front matter.")]

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, raw_text.strip(), [KBValidationError(kb_path=path.as_posix(), message="Unterminated YAML front matter.")]

    payload = "\n".join(lines[1:end_index])
    body = "\n".join(lines[end_index + 1 :]).strip()

    try:
        parsed = yaml.safe_load(payload) or {}
    except yaml.YAMLError as exc:
        return {}, body, [KBValidationError(kb_path=path.as_posix(), message=f"Invalid YAML front matter: {exc}")]

    if not isinstance(parsed, dict):
        return {}, body, [KBValidationError(kb_path=path.as_posix(), message="YAML front matter must be a mapping.")]

    return parsed, body, []


def classify_path(base_path: Path, path: Path) -> dict[str, str | None]:
    relative = path.relative_to(base_path) if path.is_relative_to(base_path) else path
    parts = relative.parts
    path_doc_kind = parts[2].lower().replace("-", "_") if len(parts) >= 3 else ""
    if len(parts) >= 4 and path_doc_kind in SUPPORTED_DOC_KINDS:
        return {
            "layout": "v2",
            "relative_path": relative.as_posix(),
            "domain": parts[0],
            "feature": parts[1],
            "doc_kind": path_doc_kind,
        }

    root = parts[0].lower() if parts else ""
    if root in LEGACY_DOC_KIND_MAPPING:
        return {
            "layout": "legacy",
            "relative_path": relative.as_posix(),
            "domain": None,
            "feature": None,
            "doc_kind": LEGACY_DOC_KIND_MAPPING[root],
        }

    return {
        "layout": "unknown",
        "relative_path": relative.as_posix(),
        "domain": None,
        "feature": None,
        "doc_kind": None,
    }


def validate_markdown_document(
    base_path: Path,
    path: Path,
    metadata: dict[str, Any],
    body: str,
) -> tuple[dict[str, Any], list[KBValidationError]]:
    path_info = classify_path(base_path, path)
    kb_path = str(path_info["relative_path"])
    errors: list[KBValidationError] = []

    if path_info["layout"] == "unknown":
        errors.append(
            KBValidationError(
                kb_path=kb_path,
                message="Unsupported KB path. Expected knowledge-base/<domain>/<feature>/<doc_kind>/<slug>.md or a legacy root.",
            )
        )
        return {}, errors

    normalized: dict[str, Any] = {
        "title": str(metadata.get("title", "")).strip(),
        "doc_kind": normalize_doc_kind(metadata.get("doc_kind") or metadata.get("doc_type") or path_info["doc_kind"]),
        "domain": str(metadata.get("domain") or path_info["domain"] or "").strip(),
        "feature": str(metadata.get("feature") or path_info["feature"] or "").strip(),
        "keywords": normalize_string_list(metadata.get("keywords")),
        "task_tags": normalize_string_list(metadata.get("task_tags")),
        "erp_versions": normalize_erp_version_list(metadata.get("erp_versions") or metadata.get("erp_version")),
        "role_scope": normalize_string_list(metadata.get("role_scope")),
        "review_status": str(metadata.get("review_status", "approved")).strip().lower(),
        "module": _none_if_blank(metadata.get("module")),
        "submenu": _none_if_blank(metadata.get("submenu")),
        "screen_id": _none_if_blank(metadata.get("screen_id")),
        "screen_title": _none_if_blank(metadata.get("screen_title")),
        "tab_name": _none_if_blank(metadata.get("tab_name")),
        "aliases": normalize_string_list(metadata.get("aliases")),
        "error_codes": normalize_string_list(metadata.get("error_codes")),
        "field_labels": normalize_string_list(metadata.get("field_labels")),
        "source_transcript_id": _none_if_blank(metadata.get("source_transcript_id")),
        "source_audio_uri": _none_if_blank(metadata.get("source_audio_uri")),
        "kb_path": kb_path,
    }

    if path_info["layout"] == "v2":
        if normalized["doc_kind"] != path_info["doc_kind"]:
            errors.append(
                KBValidationError(
                    kb_path=kb_path,
                    message=f"Path doc_kind '{path_info['doc_kind']}' does not match YAML doc_kind '{normalized['doc_kind']}'.",
                )
            )
        if normalized["domain"] != path_info["domain"]:
            errors.append(
                KBValidationError(
                    kb_path=kb_path,
                    message=f"Path domain '{path_info['domain']}' does not match YAML domain '{normalized['domain']}'.",
                )
            )
        if normalized["feature"] != path_info["feature"]:
            errors.append(
                KBValidationError(
                    kb_path=kb_path,
                    message=f"Path feature '{path_info['feature']}' does not match YAML feature '{normalized['feature']}'.",
                )
            )

        missing = [field for field in REQUIRED_FIELDS if not normalized.get(field)]
        if missing:
            errors.append(
                KBValidationError(
                    kb_path=kb_path,
                    message="Missing required metadata fields: " + ", ".join(missing),
                )
            )

    if normalized["review_status"] not in REVIEW_STATUSES:
        errors.append(
            KBValidationError(
                kb_path=kb_path,
                message=f"Invalid review_status '{normalized['review_status']}'.",
            )
        )

    body_errors = _validate_body_structure(kb_path, normalized["doc_kind"], body)
    errors.extend(body_errors)
    return normalized, errors


def normalize_review_status(value: Any, fallback: str = "approved") -> ReviewStatus:
    normalized = str(value or fallback).strip().lower()
    if normalized not in REVIEW_STATUSES:
        normalized = fallback
    return normalized  # type: ignore[return-value]


def _validate_body_structure(kb_path: str, doc_kind: str, body: str) -> list[KBValidationError]:
    lowered = body.lower()
    required_sets = {
        "how_to": ("## procedura",),
        "troubleshooting": ("## sintomo", "## risoluzione"),
    }
    if doc_kind == "reference" and "## campi" not in lowered and "## regole" not in lowered:
        return [
            KBValidationError(
                kb_path=kb_path,
                message="Reference documents must contain '## Campi' or '## Regole'.",
            )
        ]

    missing = [section for section in required_sets.get(doc_kind, ()) if section not in lowered]
    if not missing:
        return []
    return [
        KBValidationError(
            kb_path=kb_path,
            message="Missing mandatory sections: " + ", ".join(section.replace("## ", "") for section in missing),
        )
    ]


def _none_if_blank(value: Any) -> str | None:
    text = str(value or "").strip()
    return text or None
