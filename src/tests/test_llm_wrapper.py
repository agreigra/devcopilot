import pytest

from src.llm_wrapper import LLMProviderError, LLMWrapper


def test_chat_returns_mock_response_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    wrapper = LLMWrapper()

    response = wrapper.chat([{"role": "user", "content": "Bonjour"}])

    assert isinstance(response, str)
    assert "mock" in response.lower()
    assert "Bonjour" in response


def test_chat_returns_provider_response_when_available(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")

    class FakeMessage:
        content = "Réponse réelle"

    class FakeChoice:
        message = FakeMessage()

    class FakeResponse:
        choices = [FakeChoice()]

    class FakeCompletions:
        def create(self, **kwargs):
            return FakeResponse()

    class FakeChat:
        completions = FakeCompletions()

    class FakeClient:
        chat = FakeChat()

    wrapper = LLMWrapper()
    wrapper.client = FakeClient()

    response = wrapper.chat([{"role": "user", "content": "Salut"}])

    assert response == "Réponse réelle"


def test_chat_raises_controlled_error_on_provider_exception(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")

    class FakeCompletions:
        def create(self, **kwargs):
            raise RuntimeError("boom")

    class FakeChat:
        completions = FakeCompletions()

    class FakeClient:
        chat = FakeChat()

    wrapper = LLMWrapper()
    wrapper.client = FakeClient()

    with pytest.raises(LLMProviderError, match="LLM provider request failed"):
        wrapper.chat([{"role": "user", "content": "Test"}])
