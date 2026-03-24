"""Knowledge-base loading utilities for ERP manuals and SOPs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app.core.config import Settings
from app.domain.schemas import DocType, KBValidationError, ReviewStatus, SourceDocument
from app.ingestion.validators import (
    classify_path,
    normalize_doc_kind,
    normalize_review_status,
    normalize_string_list,
    parse_yaml_front_matter,
    validate_markdown_document,
)

SUPPORTED_EXTENSIONS = {".json", ".md", ".txt"}


class KnowledgeBaseLoader:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.base_path = Path(settings.knowledge_base_path)

    def load_documents(
        self,
        limit: int | None = None,
        doc_types: list[DocType] | None = None,
        erp_version: str | None = None,
        review_statuses: list[ReviewStatus] | None = None,
    ) -> list[SourceDocument]:
        documents, _, _ = self.load_documents_with_report(
            limit=limit,
            doc_types=doc_types,
            erp_version=erp_version,
            review_statuses=review_statuses,
        )
        return documents

    def load_documents_with_report(
        self,
        limit: int | None = None,
        doc_types: list[DocType] | None = None,
        erp_version: str | None = None,
        review_statuses: list[ReviewStatus] | None = None,
    ) -> tuple[list[SourceDocument], list[KBValidationError], int]:
        if not self.base_path.exists():
            return [], [], 0

        requested_doc_types = set(doc_types or [])
        requested_version = erp_version or self.settings.erp_version
        requested_review_statuses = set(review_statuses or ["approved"])
        documents: list[SourceDocument] = []
        validation_errors: list[KBValidationError] = []
        skipped_documents = 0

        for path in sorted(self.base_path.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            file_documents, file_errors = self._load_file(path)
            validation_errors.extend(file_errors)
            if file_errors and not file_documents:
                skipped_documents += 1

            for document in file_documents:
                if requested_doc_types and document.doc_kind not in requested_doc_types:
                    skipped_documents += 1
                    continue
                if requested_review_statuses and document.review_status not in requested_review_statuses:
                    skipped_documents += 1
                    continue
                if document.erp_versions and requested_version and requested_version not in document.erp_versions:
                    skipped_documents += 1
                    continue
                documents.append(document)
                if limit is not None and len(documents) >= limit:
                    return documents[:limit], validation_errors, skipped_documents

        return documents, validation_errors, skipped_documents

    def _load_file(self, path: Path) -> tuple[list[SourceDocument], list[KBValidationError]]:
        if path.suffix.lower() == ".json":
            return self._load_json(path)
        if path.suffix.lower() == ".md":
            return self._load_markdown(path)
        return self._load_text(path)

    def _load_markdown(self, path: Path) -> tuple[list[SourceDocument], list[KBValidationError]]:
        raw_text = path.read_text(encoding="utf-8")
        metadata, body, front_matter_errors = parse_yaml_front_matter(path, raw_text)
        if front_matter_errors:
            return [], front_matter_errors

        normalized, validation_errors = validate_markdown_document(self.base_path, path, metadata, body)
        if validation_errors:
            return [], validation_errors

        relative = path.relative_to(self.base_path) if path.is_relative_to(self.base_path) else path
        document = SourceDocument(
            doc_id=str(metadata.get("doc_id") or relative.as_posix()),
            title=normalized["title"],
            text=body.strip(),
            source=path.name,
            language=str(metadata.get("language") or self.settings.default_locale),
            doc_type=normalized["doc_kind"],
            doc_kind=normalized["doc_kind"],
            kb_path=normalized["kb_path"],
            domain=normalized["domain"],
            feature=normalized["feature"],
            module=normalized["module"],
            submenu=normalized["submenu"],
            screen_id=normalized["screen_id"],
            screen_title=normalized["screen_title"],
            tab_name=normalized["tab_name"],
            section_title=normalized["title"],
            heading_path=[normalized["title"]],
            field_labels=normalized["field_labels"],
            task_tags=normalized["task_tags"],
            keywords=normalized["keywords"],
            aliases=normalized["aliases"],
            error_codes=normalized["error_codes"],
            role_scope=normalized["role_scope"],
            erp_versions=normalized["erp_versions"] or [self.settings.erp_version],
            review_status=normalize_review_status(normalized["review_status"]),
            source_uri=str(metadata.get("source_uri") or relative.as_posix()),
            source_transcript_id=normalized["source_transcript_id"],
            source_audio_uri=normalized["source_audio_uri"],
        )
        return [document], []

    def _load_json(self, path: Path) -> tuple[list[SourceDocument], list[KBValidationError]]:
        payload = json.loads(path.read_text(encoding="utf-8"))
        entries = payload if isinstance(payload, list) else [payload]
        documents: list[SourceDocument] = []
        errors: list[KBValidationError] = []
        path_info = classify_path(self.base_path, path)
        kb_path = str(path_info["relative_path"])

        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                errors.append(
                    KBValidationError(
                        kb_path=kb_path,
                        message=f"JSON entry {index} must be an object.",
                    )
                )
                continue
            documents.extend(self._entry_to_documents(entry, path, index=index))

        return documents, errors

    def _load_text(self, path: Path) -> tuple[list[SourceDocument], list[KBValidationError]]:
        relative = path.relative_to(self.base_path) if path.is_relative_to(self.base_path) else path
        path_info = classify_path(self.base_path, path)
        doc_kind = normalize_doc_kind(path_info.get("doc_kind") or "overview")
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            return [], [KBValidationError(kb_path=relative.as_posix(), message="Empty text file.")]

        document = SourceDocument(
            doc_id=relative.as_posix(),
            title=path.stem.replace("_", " ").replace("-", " ").title(),
            text=text,
            source=path.name,
            language=self.settings.default_locale,
            doc_type=doc_kind,
            doc_kind=doc_kind,
            kb_path=relative.as_posix(),
            domain=path_info.get("domain"),
            feature=path_info.get("feature"),
            section_title=path.stem,
            heading_path=[path.stem],
            erp_versions=[self.settings.erp_version],
            review_status="approved",
            source_uri=relative.as_posix(),
        )
        return [document], []

    def _entry_to_documents(self, entry: dict[str, Any], path: Path, index: int) -> list[SourceDocument]:
        relative = path.relative_to(self.base_path) if path.is_relative_to(self.base_path) else path
        path_info = classify_path(self.base_path, path)
        doc_kind = normalize_doc_kind(
            entry.get("doc_kind") or entry.get("doc_type") or path_info.get("doc_kind") or "overview"
        )
        title = str(entry.get("title") or path.stem).strip()
        base_payload = {
            "doc_id": str(entry.get("doc_id") or entry.get("id") or f"{relative.as_posix()}::{index}"),
            "title": title,
            "source": path.name,
            "language": str(entry.get("language") or self.settings.default_locale),
            "doc_type": doc_kind,
            "doc_kind": doc_kind,
            "kb_path": relative.as_posix(),
            "domain": self._none_if_blank(entry.get("domain") or path_info.get("domain")),
            "feature": self._none_if_blank(entry.get("feature") or path_info.get("feature")),
            "module": self._none_if_blank(entry.get("module")),
            "submenu": self._none_if_blank(entry.get("submenu")),
            "screen_id": self._none_if_blank(entry.get("screen_id")),
            "screen_title": self._none_if_blank(entry.get("screen_title")),
            "tab_name": self._none_if_blank(entry.get("tab_name")),
            "field_labels": normalize_string_list(entry.get("field_labels")),
            "task_tags": normalize_string_list(entry.get("task_tags")),
            "keywords": normalize_string_list(entry.get("keywords")),
            "aliases": normalize_string_list(entry.get("aliases")),
            "error_codes": normalize_string_list(entry.get("error_codes")),
            "role_scope": normalize_string_list(entry.get("role_scope")),
            "erp_versions": normalize_string_list(entry.get("erp_versions") or entry.get("erp_version"))
            or [self.settings.erp_version],
            "review_status": normalize_review_status(entry.get("review_status")),
            "source_uri": str(entry.get("source_uri") or relative.as_posix()),
            "source_transcript_id": self._none_if_blank(entry.get("source_transcript_id")),
            "source_audio_uri": self._none_if_blank(entry.get("source_audio_uri")),
        }

        sections = entry.get("sections") or []
        if not sections:
            text = str(entry.get("text") or "").strip()
            if not text:
                return []
            return [
                SourceDocument(
                    **base_payload,
                    text=text,
                    section_title=str(entry.get("section_title") or title).strip() or title,
                    heading_path=[str(entry.get("section_title") or title).strip() or title],
                )
            ]

        documents: list[SourceDocument] = []
        for section_index, section in enumerate(sections):
            if not isinstance(section, dict):
                continue
            text = str(section.get("text") or "").strip()
            if not text:
                continue
            section_title = str(section.get("title") or title).strip() or title
            documents.append(
                SourceDocument(
                    **base_payload,
                    doc_id=f"{base_payload['doc_id']}::section-{section_index}",
                    text=text,
                    section_title=section_title,
                    heading_path=[section_title],
                    field_labels=normalize_string_list(section.get("field_labels")) or base_payload["field_labels"],
                    task_tags=normalize_string_list(section.get("task_tags")) or base_payload["task_tags"],
                    keywords=normalize_string_list(section.get("keywords")) or base_payload["keywords"],
                    aliases=normalize_string_list(section.get("aliases")) or base_payload["aliases"],
                    error_codes=normalize_string_list(section.get("error_codes")) or base_payload["error_codes"],
                )
            )
        return documents

    def _none_if_blank(self, value: Any) -> str | None:
        text = str(value or "").strip()
        return text or None
