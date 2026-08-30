# Ticket 02 — Implémenter `LLMWrapper`

Description

- Implémenter `src/llm_wrapper.py` avec une classe `LLMWrapper` qui expose `chat(messages: List[dict]) -> str` et supporte un mode mock si la clé LLM est absente.

Tâches

- définir interface `LLMWrapper` (init config, chat)
- implémentation minimale OpenAI (ou provider choisi) + fallback mock
- gérer timeouts et erreurs basiques
- ajouter docstring et exemples d'utilisation

Critères d'acceptation

- `LLMWrapper.chat` renvoie une string pour des messages valides
- si `OPENAI_API_KEY` absent, `chat` renvoie une réponse simulée
- erreurs du provider sont remontées sous forme d'exceptions contrôlées

Estimate: 1 jour
