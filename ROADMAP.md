# ROADMAP — DevCopilot (condensé)

Objectif général : livrer un MVP (V0) puis itérer vers agents, orchestration et production, en privilégiant apprentissage par la pratique.

- Durée estimée (approx): V0: 3–7 jours, V1: 1–2 semaines, V2: 2–3 semaines, V3: 2–3 semaines, V4: 2–4 semaines, V5: 2–4 semaines.

## Versions & livrables

### V0 — LLM Chat

- Livrables: UI `streamlit` minimale, wrapper LLM provider-agnostique, endpoint de chat.
- Critères d'acceptation: répondre à une question via l'UI; logs de requête; 2 tests unitaires (wrapper mock, endpoint).
- Tâches: init projet, dépendances, implémenter wrapper LLM, UI minimal, tests.

### V1 — Structured Output + Tool Calling

- Livrables: tools mocks (`get_project_info`, `search_tickets`, `get_service_status`), LLM capable d'appeler functions.
- Critères: LLM appelle un tool et incorpore le résultat; validation JSON-schema des outputs.

### V2 — RAG

- Livrables: pipeline ingestion (parsing → chunking → embeddings → pgvector), interface de recherche documentaire.
- Critères: retrieval pertinent pour une question d'exemple; intégration dans le prompt.

### V3 — Agent

- Livrables: agent qui orchestre plusieurs tools pour une requête complexe (ex: diagnostic service).
- Critères: agent planifie étapes, exécute outils, compile une réponse structurée.

### V4 — Orchestration

- Livrables: orchestrateur de workflows (conditionnels, retries, timeout, validation humaine).
- Critères: workflow d'exemple fonctionnel avec retries et validation humaine.

### V5 — Production

- Livrables: Docker, tests élargis, observability, sécurité (permissions, prompt-injection mitigation).
- Critères: container deployable localement/cloud, tests d'intégration, monitoring tokens/cost.

## Cross-cutting

- Tests unitaires et mocks pour interactions LLM/tools.
- Timeouts, retries, validation JSON Schema, whitelisting tools sensibles.
- Logging requests/responses + durées; metrics tokens/cost.
- Documentation: `README.md`, `devcopilot/ROADMAP.md`, notes d'architecture.

## Priorités immédiates

1. Livrer V0 fonctionnel et testé.
2. Ajouter function-calling (V1).
3. Mettre en place RAG si connaissances internes nécessaires (V2).

## Risques & mitigations

- Coût API élevé → limiter tokens, cacher réponses, batcher.
- Hallucinations → contexte RAG, validation et citations.
- Secrets exposés → variables d'environnement, `.gitignore`.

---

Prochaine étape recommandée : implémenter V0 (cahier des charges + arborescence + dépendances + exercise). Je peux générer ces éléments maintenant.
