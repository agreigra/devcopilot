import os
from typing import Any, List


class LLMProviderError(RuntimeError):
    """Raised when the configured LLM provider fails."""


class LLMWrapper:
    """Thin provider-agnostic wrapper around a chat-based LLM client.

    If no API key is configured, the wrapper falls back to a mock response so
    local development and tests remain usable without external credentials.
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "gpt-4o-mini",
        timeout: int = 30,
        client: Any | None = None,
    ) -> None:
        self.api_key = (api_key or os.getenv("OPENAI_API_KEY") or "").strip()
        self.model = model
        self.timeout = timeout
        self.client = client

    def _mock_response(self, messages: List[dict]) -> str:
        if not messages:
            return "Mock LLM response: no input provided."

        for message in messages:
            content = message.get("content") if isinstance(message, dict) else None
            if message.get("role") == "user" and content:
                return f"Mock LLM response for: {content}"

        last_message = messages[-1]
        content = last_message.get("content") if isinstance(last_message, dict) else str(last_message)
        return f"Mock LLM response for: {content}"

    def chat(self, messages: List[dict]) -> str:
        """Send a list of chat messages to the current LLM provider.

        Returns a string response. If no API key is configured, a local mock
        response is returned to keep the app functional in development.
        """
        if not isinstance(messages, list) or not messages:
            raise ValueError("messages must be a non-empty list of dictionaries")

        if not self.api_key:
            return self._mock_response(messages)

        if self.client is None:
            try:
                from openai import OpenAI
            except ImportError as exc:  # pragma: no cover - dependency guard
                raise LLMProviderError("OpenAI client is not installed") from exc

            self.client = OpenAI(api_key=self.api_key, timeout=self.timeout)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                timeout=self.timeout,
            )
            content = response.choices[0].message.content
            if content is None:
                return ""
            return str(content)
        except Exception as exc:
            raise LLMProviderError("LLM provider request failed") from exc


__all__ = ["LLMWrapper", "LLMProviderError"]
