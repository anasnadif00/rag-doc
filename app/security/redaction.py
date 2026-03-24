"""Redaction helpers for sensitive ERP screen data."""

from __future__ import annotations

import re

from app.domain.schemas import FieldContext, RecordContext, RedactionResult, ScreenContext

SENSITIVE_HINTS = (
    "password",
    "iban",
    "conto",
    "bank",
    "partita iva",
    "fiscale",
    "indirizzo",
    "address",
    "telefono",
    "email",
    "mail",
)
SENSITIVE_VALUE_PATTERNS = (
    re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    re.compile(r"(?<!\w)\+?\d[\d\s-]{8,}\d(?!\w)"),
    re.compile(r"\b\d{11,16}\b"),
)


def _mask_value(value: str) -> str:
    if len(value) <= 4:
        return "*" * len(value)
    return f"{value[:2]}{'*' * (len(value) - 4)}{value[-2:]}"


def _mask_sensitive_text(value: str) -> tuple[str, bool]:
    redacted = value
    modified = False
    for pattern in SENSITIVE_VALUE_PATTERNS:
        redacted, count = pattern.subn(lambda match: _mask_value(match.group(0)), redacted)
        modified = modified or count > 0
    return redacted, modified


def _is_sensitive_field(field: FieldContext, allowlist: set[str], denylist: set[str]) -> bool:
    label_tokens = " ".join(filter(None, [field.field_id or "", field.label])).lower()
    if any(item in label_tokens for item in allowlist):
        return False
    if any(item in label_tokens for item in denylist):
        return True
    return field.is_sensitive or any(hint in label_tokens for hint in SENSITIVE_HINTS)


def _redact_record(
    record: RecordContext | None,
    allowlist: set[str],
    denylist: set[str],
) -> tuple[RecordContext | None, list[str]]:
    if record is None:
        return None, []

    values: dict[str, str | int | float | bool | None] = {}
    redacted_fields: list[str] = []
    for key, value in record.values.items():
        lowered_key = key.lower()
        if any(item in lowered_key for item in allowlist):
            values[key] = value
            continue

        is_sensitive = any(item in lowered_key for item in denylist) or any(
            hint in lowered_key for hint in SENSITIVE_HINTS
        )
        if is_sensitive and value is not None:
            values[key] = _mask_value(str(value))
            redacted_fields.append(key)
        elif isinstance(value, str):
            masked, modified = _mask_sensitive_text(value)
            values[key] = masked
            if modified:
                redacted_fields.append(key)
        else:
            values[key] = value

    primary_label = record.primary_label
    if primary_label:
        primary_label, modified = _mask_sensitive_text(primary_label)
        if modified:
            redacted_fields.append("selected_record.primary_label")

    return (
        RecordContext(
            record_id=record.record_id,
            primary_label=primary_label,
            values=values,
        ),
        redacted_fields,
    )


def redact_screen_context(
    screen_context: ScreenContext,
    allowlist: tuple[str, ...] = (),
    denylist: tuple[str, ...] = (),
) -> RedactionResult:
    allowlist_set = {item.lower() for item in allowlist}
    denylist_set = {item.lower() for item in denylist}

    redacted_fields: list[str] = []
    fields: list[FieldContext] = []
    for field in screen_context.fields:
        sensitive = _is_sensitive_field(field, allowlist_set, denylist_set)
        raw_value = field.value
        masked_value = field.masked_value

        if sensitive and raw_value:
            masked_value = masked_value or _mask_value(raw_value)
            raw_value = None
            redacted_fields.append(field.label)
        elif raw_value:
            raw_value, modified = _mask_sensitive_text(raw_value)
            if modified:
                redacted_fields.append(field.label)
        elif masked_value:
            masked_value, _ = _mask_sensitive_text(masked_value)

        fields.append(
            FieldContext(
                field_id=field.field_id,
                label=field.label,
                value=raw_value,
                masked_value=masked_value,
                is_sensitive=sensitive,
                is_required=field.is_required,
                is_editable=field.is_editable,
                validation_error=field.validation_error,
            )
        )

    notice = None
    if redacted_fields:
        notice = (
            "Alcuni valori sensibili della schermata sono stati mascherati "
            "prima di inviare il contesto al modello."
        )

    free_text_context = screen_context.free_text_context
    if free_text_context:
        free_text_context, modified = _mask_sensitive_text(free_text_context)
        if modified:
            redacted_fields.append("free_text_context")

    error_messages: list[str] = []
    for message in screen_context.error_messages:
        masked_message, modified = _mask_sensitive_text(message)
        error_messages.append(masked_message)
        if modified:
            redacted_fields.append("error_messages")

    selected_record, selected_record_redactions = _redact_record(
        screen_context.selected_record,
        allowlist_set,
        denylist_set,
    )
    redacted_fields.extend(selected_record_redactions)

    if redacted_fields and notice is None:
        notice = (
            "Alcuni valori sensibili della schermata sono stati mascherati "
            "prima di inviare il contesto al modello."
        )

    return RedactionResult(
        screen_context=ScreenContext(
            application=screen_context.application,
            module=screen_context.module,
            submenu=screen_context.submenu,
            screen_id=screen_context.screen_id,
            screen_title=screen_context.screen_title,
            tab_name=screen_context.tab_name,
            breadcrumb=screen_context.breadcrumb,
            current_action=screen_context.current_action,
            error_messages=error_messages,
            free_text_context=free_text_context,
            fields=fields,
            selected_record=selected_record,
            table_context=screen_context.table_context,
        ),
        redacted_fields=list(dict.fromkeys(redacted_fields)),
        notice=notice,
    )
