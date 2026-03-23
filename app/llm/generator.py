"""Answer generation using OpenAI chat completions."""

from __future__ import annotations

from openai import OpenAI

from app.core.config import Settings
from app.domain.schemas import QuerySource


class AnswerGenerator:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate(self, question: str, sources: list[QuerySource]) -> str:
        context_blocks = []
        for index, source in enumerate(sources, start=1):
            context_blocks.append(
                "\n".join(
                    [
                        f"[Source {index}]",
                        f"Title: {source.title}",
                        f"Origin: {source.source}",
                        f"Language: {source.language}",
                        f"Content: {source.text}",
                    ]
                )
            )
        context = "\n\n".join(context_blocks)

        completion = self.client.chat.completions.create(
            model=self.settings.generation_model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You answer questions using only the provided context. "
                        "If the context is insufficient, say so plainly."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Question:\n{question}\n\n"
                        f"Context:\n{context}"
                    ),
                },
            ],
        )
        message = completion.choices[0].message.content
        return message.strip() if message else "I could not generate an answer from the retrieved context."
