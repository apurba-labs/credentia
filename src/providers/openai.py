from __future__ import annotations

from typing import Type

from pydantic import BaseModel

from src.core.ai_client import AIClient

from typing import TypeVar

T = TypeVar("T", bound=BaseModel)

class OpenAIProvider:
    """
    High-level provider for AI-powered capabilities.

    This class intentionally contains no business logic.
    It simply delegates prompt execution to the AI client.
    """

    def __init__(self, client: AIClient | None = None) -> None:
        self.client = client or AIClient()

    def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[BaseModel],
    ) -> T:
        """
        Generate structured output from OpenAI.
        """

        return self.client.generate_json(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=response_model,
        )