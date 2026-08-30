# Contexte

Je suis développeur backend avec environ 5 ans d'expérience en Java / Spring Boot et React. J'ai également des bases en IA/NLP/ML : tokens, embeddings, tokenization, supervised/unsupervised learning, SVM, NLP, etc.

Mon objectif est de monter rapidement en compétence sur l'AI Engineering, notamment :

- LLM
- prompting
- structured outputs
- tool/function calling
- RAG
- agents
- orchestration
- memory/state
- guardrails
- observability
- productionisation

Je veux apprendre principalement **par la pratique**, en construisant un projet réel.

# Projet

Je veux construire un MVP appelé **DevCopilot**.

C'est un assistant AI destiné à une équipe de développement.

À terme, il devra pouvoir :

- répondre à des questions techniques
- rechercher dans une documentation interne
- rechercher des tickets
- consulter des informations sur des services
- analyser des logs
- utiliser plusieurs tools
- choisir dynamiquement les tools nécessaires
- orchestrer plusieurs étapes pour résoudre un problème
- demander une validation humaine avant certaines actions

# Stack initiale

Pour le MVP, je veux volontairement utiliser Python afin d'aller rapidement sur la partie AI.

- Python
- Streamlit pour l'interface
- API d'un LLM (commencer avec un seul provider)
- PostgreSQL
- pgvector
- Docker lorsque cela devient pertinent

Je ne veux PAS commencer par React ou Spring Boot.

L'interface Streamlit est uniquement une interface MVP. La logique métier et AI doit être suffisamment bien séparée pour pouvoir remplacer Streamlit plus tard.

# Ta mission

Agis comme mon **AI Tech Lead + mentor**, pas comme un simple générateur de code.

Je veux construire le projet progressivement.

Nous allons suivre cette progression :

## V0 — LLM Chat

Streamlit → Python → LLM → réponse

Objectifs :

- appeler un LLM
- gérer les prompts
- comprendre system/user messages
- gérer le contexte conversationnel
- streaming si pertinent
- gérer erreurs et configuration

## V1 — Structured Output + Tool Calling

Ajouter quelques tools simples :

- get_project_info()
- search_tickets()
- get_service_status()

Le LLM doit pouvoir décider quand appeler un tool.

Objectifs :

- comprendre function/tool calling
- comprendre les arguments structurés
- gérer les résultats de tools
- comprendre la boucle agent → tool → agent

## V2 — RAG

Ajouter une documentation :

documents/

- architecture.md
- authentication.md
- deployment.md
- database.md

Pipeline :

documents
→ parsing
→ chunking
→ embeddings
→ pgvector
→ retrieval
→ context
→ LLM

Objectifs :

- comprendre concrètement RAG
- choisir une stratégie de chunking
- metadata
- similarity search
- retrieval quality
- hallucinations
- citations/sources

## V3 — Agent

Combiner plusieurs tools :

- documentation search
- ticket search
- service status
- logs

L'agent doit pouvoir décider quels tools utiliser pour répondre à une question complexe.

Exemple :

"Pourquoi le service payment est-il lent depuis ce matin ?"

L'agent pourrait :

1. vérifier le statut du service
2. rechercher les logs
3. rechercher les tickets
4. consulter la documentation
5. analyser les résultats
6. produire une réponse

## V4 — Orchestration

Introduire explicitement un orchestrateur.

Le workflow devra gérer :

- étapes conditionnelles
- plusieurs agents/tools
- parallélisation lorsque pertinente
- retries
- timeout
- erreurs
- état du workflow
- validation humaine
- arrêt/reprise

Je veux comprendre la différence entre :

LLM → Tool calling → Agent → Workflow → Orchestrator.

## V5 — Production

Ajouter progressivement :

- logging
- tracing
- observability
- token/cost tracking
- sécurité
- prompt injection protection
- permissions des tools
- validation des outputs
- Docker
- tests
- evaluation des réponses

# Règles importantes pour m'accompagner

1. **Ne me donne pas tout le projet d'un coup.**

On avance étape par étape.

2. Pour chaque étape :
   - explique brièvement le concept
   - donne-moi l'objectif
   - donne-moi les tâches à réaliser
   - propose une architecture simple
   - indique les pièges à éviter
   - puis laisse-moi coder

3. Si je te demande du code, donne-moi uniquement le code nécessaire pour l'étape actuelle.

4. Ne complexifie pas prématurément l'architecture.

Je préfère :

solution simple → comprendre → améliorer → productioniser.

# Contexte (version révisée)

Je suis développeur backend avec ~5 ans d'expérience (Java / Spring Boot et React). J'ai des bases en IA/NLP/ML (tokens, embeddings, tokenization, supervised/unsupervised learning, SVM, NLP, ...).

Objectif principal : monter rapidement en compétence sur l'AI Engineering en construisant un projet réel étape par étape.

# Vision du projet

MVP : **DevCopilot** — assistant AI pour une équipe de développement.

Fonctionnalités à terme (non exhaustif) :

- répondre à des questions techniques
- rechercher dans une documentation interne
- rechercher/des lier des tickets
- consulter l'état des services
- analyser des logs
- utiliser et orchestrer plusieurs tools
- demander validation humaine pour actions sensibles

# Définitions rapides (pour éviter les confusions)

- `LLM` : le modèle de langage utilisé pour générer/compréter du texte.
- `Tool/Function` : une API ou fonction externe que l'agent peut appeler (ex : `get_service_status(service_name)`).
- `Agent` : composant décisionnel qui interagit avec un LLM et appelle des tools pour accomplir une tâche.
- `Workflow` : suite d'étapes (conditionnelles ou non) pour résoudre une demande complexe.
- `Orchestrator` : composant gérant l'exécution/coordonation de workflows et agents (retries, parallélisation, état).

# Contraintes et principes pédagogiques (inchangés)

- Avancer étape par étape (V0 → V5).
- Favoriser la pratique : code, debugging, tests, petits exercices.
- Préférer une solution simple d'abord ; productioniser ensuite.
- UI MVP : Streamlit (séparée clairement de la logique AI/business).
- Choisir un seul framework/paradigme quand pertinent.

# Ajouts et clarifications (révision)

1. Critères d'acceptation (exemples mesurables)

- V0 : l'application Streamlit prend une question utilisateur, appelle un wrapper LLM, affiche la réponse et renvoie un code 200. Couvrir par 2 tests unitaires : wrapper LLM (mock) et endpoint Streamlit minimal.
- V1 : le LLM peut déclencher au moins une fonction tool et le résultat est incorporé dans la réponse. Tester la décision de call (mock LLM).
- V2 : un document est ingéré, stocké dans `pgvector` et retrouvé par similarité pour un exemple de question.

2. Signatures exemples pour les tools (claires et typées)

- `get_project_info() -> dict` # renvoie métadonnées du projet
- `search_tickets(query: str, limit: int=5) -> List[Ticket]`
- `get_service_status(service_name: str) -> {"status": "ok|degraded|down","uptime": float, "meta": {}}`

3. Provider LLM initial (recommandation)

- Commencer par **OpenAI** (API bien documentée) ou un provider équivalent. Implémenter un wrapper provider-agnostique permettant de remplacer le provider plus tard.

4. Sécurité & robustesse minimales

- Timeouts et retries configurables pour chaque call LLM/tool.
- Permissions/whitelist pour les tools sensibles.
- Validation structurelle des outputs (JSON Schema pour outputs structurés).
- Défenses basiques contre prompt injection (sanitization des inputs, templates fermés pour system prompts).

5. Tests et CI

- Tests unitaires pour : wrapper LLM (mock), logique d'appel de tools (mock), pipeline de retrieval minimal (mock embeddings).
- Checklist CI minimal : lint, pytest (subset), checks basiques de sécurité (no secrets committed).

6. Scénarios utilisateurs (exemples)

- Q1: "Est-ce que le service payment est en panne ?" → LLM doit appeler `get_service_status(payment)` puis synthétiser.
- Q2: "Trouve le ticket lié au déploiement du service X" → LLM doit appeler `search_tickets("deployment service X")` puis présenter les résultats.

7. Observabilité & coûts

- Logging minimal (requests LLM + tool calls + durations).
- Metrics pour compter tokens/coûts par requête (estimations) et empêcher dépassement.

8. Format et ressources initiales

- `documents/` : fichiers Markdown (architecture.md, authentication.md, deployment.md, database.md) — fournir quelques fichiers d'exemple pour V2.

# Organisation des versions (résumé)

- V0 — LLM Chat (Streamlit + wrapper LLM).
- V1 — Structured Output + Tool Calling.
- V2 — RAG (embeddings → pgvector → retrieval).
- V3 — Agent (choix dynamique de tools, pipeline d'investigation).
- V4 — Orchestration (workflows, retries, parallélisation, validation humaine).
- V5 — Production (logging, tracing, sécurité, tests, Docker).

# Exigences pour accompagner (ce que j'attends de toi)

1. Ne pas livrer tout le projet en une fois — avancer étape par étape.
2. Pour chaque étape : explication brève du concept, objectif, tâches, architecture simple, pièges, puis te laisser coder.
3. Si code demandé, fournir uniquement le code nécessaire pour l'étape courante.
4. Quand plusieurs options existent, en choisir une et expliquer le pourquoi.
5. Challenger les choix techniques si nécessaire.
6. À la fin de chaque étape, lister ce que j'ai appris.

# Première tâche (rappel)

Commencer uniquement par **V0**.
Pour V0 fournir :

1. Cahier des charges minimal
2. Arborescence du projet
3. Dépendances nécessaires
4. Variables d'environnement nécessaires
5. Étapes d'implémentation dans l'ordre
6. Un premier exercice à coder

---

Cette version révisée clarifie les critères d'acceptation, ajoute des signatures de tools exemples, fixe des exigences minimales de sécurité/tests et donne des scénarios utilisateurs concrets pour guider le développement.
