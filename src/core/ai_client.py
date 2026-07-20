from __future__ import annotations

import json
import logging
from typing import Type

from openai import OpenAI
from pydantic import BaseModel, ValidationError

from .config import get_settings

settings = get_settings()

logger = logging.getLogger(__name__)

class AIClient:
    """
    Thin wrapper around the OpenAI Responses API.

    Responsibilities:
    - Authenticate
    - Send requests
    - Parse structured JSON
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
    ) -> None:

        self.api_key = api_key or settings.openai_api_key
        self.model = model or settings.openai_model

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not configured.")

        self.client = OpenAI(
            api_key=self.api_key,
            timeout=60.0,
        )

    def generate_json(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        response_model: Type[BaseModel],
    ) -> BaseModel:
        """
        Ask the model for JSON matching a Pydantic model.
        """

        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        text = response.output_text

        try:
            data = json.loads(text)
            logger.info(
                "OpenAI response received using model '%s'.",
                self.model,
            )
            return response_model.model_validate(data)

        except json.JSONDecodeError as exc:
            logger.exception(
                "OpenAI model '%s' returned invalid JSON.",
                self.model,
            )
            raise RuntimeError("Invalid JSON returned from OpenAI.") from exc

        except ValidationError as exc:
            logger.exception("Response validation failed.")
            logger.exception(
                "OpenAI model '%s' Response validation failed.",
                self.model,
            )
            raise RuntimeError("OpenAI response does not match schema.") from exc