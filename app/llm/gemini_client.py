from __future__ import annotations

import json
from collections.abc import AsyncGenerator

import httpx
from httpx_sse import aconnect_sse

from app.models.gemini_models import (
    GenerateContentRequest,
    GenerateContentResponse,
)

class GeminiClient:
    """
    An asynchronous client for the Gemini API.

    Handles both unary and streaming (SSE) content generation.
    """

    def __init__(
        self,
        api_key: str,
        model_name: str = "gemini-2.5-flash",
        base_url: str = "https://generativelanguage.googleapis.com/v1beta",
    ):
        """
        Initialize the GeminiClient.

        Args:
            api_key: Your Google AI Studio API key.
            model_name: The Gemini model to use (e.g., 'gemini-2.5-flash').
            base_url: The base REST API URL.
        """
        self.api_key = api_key
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")

    def _build_url(self, method: str) -> str:
        """Construct the REST URL for a specific model method."""
        return f"{self.base_url}/models/{self.model_name}:{method}?key={self.api_key}"

    async def generate_content(
        self,
        request: GenerateContentRequest,
        client: httpx.AsyncClient | None = None,
    ) -> GenerateContentResponse:
        """
        Send a single request to Gemini to generate content.

        Args:
            request: The validated GenerateContentRequest model.
            client: Optional existing httpx.AsyncClient.

        Returns:
            A validated GenerateContentResponse model.
        """
        url = self._build_url("generateContent")
        payload = request.model_dump(by_alias=True, exclude_none=True)

        if client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            return GenerateContentResponse.model_validate(response.json())

        async with httpx.AsyncClient(timeout=30.0) as c:
            response = await c.post(url, json=payload)
            response.raise_for_status()
            return GenerateContentResponse.model_validate(response.json())
