"""Answer generation using OpenAI chat completions."""

from __future__ import annotations

import json

from openai import OpenAI

from app.core.config import Settings
from app.core.prompts import ERP_SYSTEM_PROMPT, build_user_prompt
from app.domain.schemas import GeneratedAnswer, QueryPlan, QuerySource, ScreenContext


class AnswerGenerator:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate(
        self,
        message: str,
        screen_context: ScreenContext,
        query_plan: QueryPlan,
        sources: list[QuerySource],
    ) -> GeneratedAnswer:
        prompt = build_user_prompt(
            message=message,
            screen_context=screen_context,
            query_plan=query_plan,
            sources=sources,
            max_context_chars=self.settings.max_context_chars,
        )
        completion = self.client.chat.completions.create(
            model=self.settings.generation_model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": ERP_SYSTEM_PROMPT,
                },
                {"role": "user", "content": prompt},
            ],
        )
        message = completion.choices[0].message.content
        return self._parse_response(message or "")

    def _parse_response(self, raw_message: str) -> GeneratedAnswer:
        content = raw_message.strip()
        if content.startswith("```"):
            content = content.strip("`")
            if content.startswith("json"):
                content = content[4:].strip()

        try:
            payload = json.loads(content)
        except json.JSONDecodeError:
            return GeneratedAnswer(answer=raw_message.strip(), steps=[], answer_mode="grounded")

        confidence = payload.get("confidence")
        if confidence is not None:
            try:
                confidence = float(confidence)
            except (TypeError, ValueError):
                confidence = None

        answer_mode = str(payload.get("answer_mode") or "grounded").strip().lower()
        if answer_mode not in {"grounded", "partial_inference", "clarification"}:
            answer_mode = "grounded"

        return GeneratedAnswer(
            answer=str(payload.get("answer", "")).strip(),
            steps=[str(item).strip() for item in payload.get("steps", []) if str(item).strip()],
            follow_up_question=payload.get("follow_up_question"),
            confidence=confidence,
            answer_mode=answer_mode,  # type: ignore[arg-type]
            inference_notice=payload.get("inference_notice"),
        )
