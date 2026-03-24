"""Document-type-aware chunking for ERP Markdown knowledge."""

from __future__ import annotations

import re
from typing import Any

from app.domain.schemas import ChunkRecord, SourceDocument

STEP_PATTERN = re.compile(r"^\s*(\d+)[\.\)]\s+(.*)$")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.*)$")


class MarkdownChunker:
    def chunk_documents(self, documents: list[SourceDocument], ingested_at: str) -> list[ChunkRecord]:
        chunks: list[ChunkRecord] = []
        for document in documents:
            chunks.extend(self.chunk_document(document, ingested_at))
        return chunks

    def chunk_document(self, document: SourceDocument, ingested_at: str) -> list[ChunkRecord]:
        sections = self._parse_sections(document.text)
        if document.doc_kind == "how_to":
            records = self._chunk_how_to(document, sections, ingested_at)
        elif document.doc_kind == "troubleshooting":
            records = self._chunk_troubleshooting(document, sections, ingested_at)
        elif document.doc_kind == "reference":
            records = self._chunk_reference(document, sections, ingested_at)
        else:
            records = self._chunk_generic(document, sections, ingested_at)

        return records or [self._build_chunk(document, document.text.strip(), ingested_at, chunk_kind="section")]

    def _chunk_how_to(
        self,
        document: SourceDocument,
        sections: list[dict[str, Any]],
        ingested_at: str,
    ) -> list[ChunkRecord]:
        chunks: list[ChunkRecord] = []
        intro_sections = self._find_sections(sections, "", include_empty_path=True)
        prerequisites = self._find_sections(sections, "Prerequisiti")
        overview_text = self._join_text_blocks(intro_sections + prerequisites)
        if overview_text:
            chunks.append(
                self._build_chunk(
                    document,
                    overview_text,
                    ingested_at,
                    heading_path=["Panoramica"],
                    chunk_kind="overview",
                )
            )

        procedure_sections = self._find_sections(sections, "Procedura")
        procedure_text = self._join_text_blocks(procedure_sections)
        steps = self._parse_steps(procedure_text)
        if not steps and procedure_text:
            return chunks + self._chunk_generic(document, procedure_sections, ingested_at, chunk_kind="procedure")

        start_index = 0
        while start_index < len(steps):
            group: list[tuple[int, str]] = []
            token_budget = 0
            while start_index < len(steps) and len(group) < 3:
                step = steps[start_index]
                step_tokens = self._estimate_tokens(step[1])
                if group and token_budget + step_tokens > 450:
                    break
                group.append(step)
                token_budget += step_tokens
                start_index += 1

            if not group:
                group.append(steps[start_index])
                start_index += 1

            rendered = "\n".join(f"{index}. {text}" for index, text in group)
            chunks.append(
                self._build_chunk(
                    document,
                    rendered,
                    ingested_at,
                    heading_path=["Procedura"],
                    chunk_kind="procedure",
                    step_start=group[0][0],
                    step_end=group[-1][0],
                    section_title="Procedura",
                )
            )

        final_checks = self._find_sections(sections, "Verifiche finali")
        final_text = self._join_text_blocks(final_checks)
        if final_text:
            chunks.append(
                self._build_chunk(
                    document,
                    final_text,
                    ingested_at,
                    heading_path=["Verifiche finali"],
                    chunk_kind="verification",
                    section_title="Verifiche finali",
                )
            )
        return chunks

    def _chunk_troubleshooting(
        self,
        document: SourceDocument,
        sections: list[dict[str, Any]],
        ingested_at: str,
    ) -> list[ChunkRecord]:
        chunks: list[ChunkRecord] = []
        symptom_text = self._join_text_blocks(self._find_sections(sections, "Sintomo"))
        causes_text = self._join_text_blocks(self._find_sections(sections, "Cause probabili"))
        if symptom_text or causes_text:
            chunks.append(
                self._build_chunk(
                    document,
                    "\n\n".join(part for part in (symptom_text, causes_text) if part),
                    ingested_at,
                    heading_path=["Sintomo", "Cause probabili"] if causes_text else ["Sintomo"],
                    chunk_kind="symptom",
                    section_title="Sintomo",
                )
            )

        resolution_text = self._join_text_blocks(self._find_sections(sections, "Risoluzione"))
        if resolution_text:
            chunks.append(
                self._build_chunk(
                    document,
                    resolution_text,
                    ingested_at,
                    heading_path=["Risoluzione"],
                    chunk_kind="resolution",
                    section_title="Risoluzione",
                )
            )

        escalation_text = self._join_text_blocks(self._find_sections(sections, "Quando escalare"))
        if escalation_text:
            chunks.append(
                self._build_chunk(
                    document,
                    escalation_text,
                    ingested_at,
                    heading_path=["Quando escalare"],
                    chunk_kind="escalation",
                    section_title="Quando escalare",
                )
            )
        return chunks

    def _chunk_reference(
        self,
        document: SourceDocument,
        sections: list[dict[str, Any]],
        ingested_at: str,
    ) -> list[ChunkRecord]:
        chunks: list[ChunkRecord] = []
        for section_name in ("Campi", "Regole"):
            for section in self._find_sections(sections, section_name):
                nested = self._extract_nested_subsections(section["text"])
                if nested:
                    for nested_title, nested_text in nested:
                        chunks.append(
                            self._build_chunk(
                                document,
                                nested_text,
                                ingested_at,
                                heading_path=[section_name, nested_title],
                                chunk_kind="reference",
                                section_title=nested_title,
                            )
                        )
                    continue

                chunks.append(
                    self._build_chunk(
                        document,
                        section["text"],
                        ingested_at,
                        heading_path=section["heading_path"] or [section_name],
                        chunk_kind="reference",
                        section_title=section_name,
                    )
                )
        return chunks

    def _chunk_generic(
        self,
        document: SourceDocument,
        sections: list[dict[str, Any]],
        ingested_at: str,
        chunk_kind: str = "section",
    ) -> list[ChunkRecord]:
        chunks: list[ChunkRecord] = []
        if not sections:
            text = document.text.strip()
            if text:
                chunks.append(self._build_chunk(document, text, ingested_at, chunk_kind=chunk_kind))
            return chunks

        for section in sections:
            text = section["text"].strip()
            if not text:
                continue
            chunks.append(
                self._build_chunk(
                    document,
                    text,
                    ingested_at,
                    heading_path=section["heading_path"],
                    chunk_kind=chunk_kind,
                    section_title=section["title"] or document.section_title or document.title,
                )
            )
        return chunks

    def _build_chunk(
        self,
        document: SourceDocument,
        text: str,
        ingested_at: str,
        heading_path: list[str] | None = None,
        chunk_kind: str | None = None,
        step_start: int | None = None,
        step_end: int | None = None,
        section_title: str | None = None,
    ) -> ChunkRecord:
        heading_path = [part for part in (heading_path or []) if part]
        chunk_id = self._build_chunk_id(document.doc_id, heading_path, step_start, step_end)
        return ChunkRecord(
            chunk_id=chunk_id,
            doc_id=document.doc_id,
            title=document.title,
            text=text.strip(),
            source=document.source,
            language=document.language,
            doc_type=document.doc_type,
            doc_kind=document.doc_kind,
            kb_path=document.kb_path,
            domain=document.domain,
            feature=document.feature,
            module=document.module,
            submenu=document.submenu,
            screen_id=document.screen_id,
            screen_title=document.screen_title,
            tab_name=document.tab_name,
            section_title=section_title or document.section_title or document.title,
            heading_path=heading_path,
            chunk_kind=chunk_kind or document.chunk_kind,
            step_start=step_start,
            step_end=step_end,
            field_labels=document.field_labels,
            task_tags=document.task_tags,
            keywords=document.keywords,
            aliases=document.aliases,
            error_codes=document.error_codes,
            role_scope=document.role_scope,
            erp_versions=document.erp_versions,
            review_status=document.review_status,
            source_uri=document.source_uri,
            token_estimate=self._estimate_tokens(text),
            ingested_at=ingested_at,
        )

    def _parse_sections(self, text: str) -> list[dict[str, Any]]:
        sections: list[dict[str, Any]] = []
        heading_stack: list[tuple[int, str]] = []
        current_lines: list[str] = []
        current_title: str | None = None
        current_path: list[str] = []

        def flush() -> None:
            nonlocal current_lines
            body = "\n".join(current_lines).strip()
            if body or current_title is not None:
                sections.append(
                    {
                        "title": current_title,
                        "heading_path": list(current_path),
                        "text": body,
                    }
                )
            current_lines = []

        for line in text.splitlines():
            match = HEADING_PATTERN.match(line.strip())
            if not match:
                current_lines.append(line)
                continue

            flush()
            level = len(match.group(1))
            title = match.group(2).strip()
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()
            heading_stack.append((level, title))
            current_title = title
            current_path = [item for _, item in heading_stack]

        flush()
        return sections

    def _find_sections(
        self,
        sections: list[dict[str, Any]],
        title: str,
        include_empty_path: bool = False,
    ) -> list[dict[str, Any]]:
        lowered = title.lower()
        matches = []
        for section in sections:
            section_title = (section["title"] or "").lower()
            if include_empty_path and not section["heading_path"] and section["text"].strip():
                matches.append(section)
                continue
            if lowered and section_title == lowered:
                matches.append(section)
        return matches

    def _extract_nested_subsections(self, text: str) -> list[tuple[str, str]]:
        nested: list[tuple[str, str]] = []
        current_title: str | None = None
        current_lines: list[str] = []
        for line in text.splitlines():
            if line.startswith("### "):
                body = "\n".join(current_lines).strip()
                if current_title and body:
                    nested.append((current_title, body))
                current_title = line.removeprefix("### ").strip()
                current_lines = []
                continue
            current_lines.append(line)

        body = "\n".join(current_lines).strip()
        if current_title and body:
            nested.append((current_title, body))
        return nested

    def _join_text_blocks(self, sections: list[dict[str, Any]]) -> str:
        return "\n\n".join(section["text"].strip() for section in sections if section["text"].strip())

    def _parse_steps(self, text: str) -> list[tuple[int, str]]:
        if not text:
            return []

        steps: list[tuple[int, str]] = []
        current_index: int | None = None
        current_lines: list[str] = []

        def flush() -> None:
            nonlocal current_index, current_lines
            body = "\n".join(current_lines).strip()
            if current_index is not None and body:
                steps.append((current_index, body))
            current_index = None
            current_lines = []

        for line in text.splitlines():
            match = STEP_PATTERN.match(line)
            if match:
                flush()
                current_index = int(match.group(1))
                current_lines = [match.group(2).strip()]
                continue
            if current_index is not None:
                current_lines.append(line.strip())

        flush()
        return steps

    def _build_chunk_id(
        self,
        doc_id: str,
        heading_path: list[str],
        step_start: int | None,
        step_end: int | None,
    ) -> str:
        slug_parts = [self._slugify(part) for part in heading_path if part]
        suffix = ".".join(part for part in slug_parts if part)
        if step_start is not None:
            suffix = f"{suffix}.steps-{step_start}-{step_end}" if suffix else f"steps-{step_start}-{step_end}"
        if not suffix:
            suffix = "chunk"
        return f"{doc_id}::{suffix}"

    def _slugify(self, value: str) -> str:
        cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
        return cleaned or "section"

    def _estimate_tokens(self, text: str) -> int:
        return max(1, len(text) // 4)
