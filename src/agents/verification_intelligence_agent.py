from __future__ import annotations

from src.models.intelligence import VerificationIntelligence
from src.prompts.verification_intelligence import (
    SYSTEM_PROMPT,
    build_user_prompt,
)
from src.providers.openai import OpenAIProvider


class VerificationIntelligenceAgent:
    """
    Generates an AI-powered explanation of a completed verification.

    This agent never changes verification outcomes. It only explains
    deterministic results using the structured verification data.
    """

    def __init__(
        self,
        provider: OpenAIProvider | None = None,
    ) -> None:
        self.provider = provider or OpenAIProvider()

    def generate(
        self,
        payload: dict,
    ) -> VerificationIntelligence:
        """
        Generate an executive intelligence report from structured
        verification data.
        """

        return self.provider.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=build_user_prompt(payload),
            response_model=VerificationIntelligence,
        )