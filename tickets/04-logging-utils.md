# Ticket 04 — Logging et utilitaires

Description

- Ajouter `src/utils.py` pour logging basique (timestamp, durée, erreurs) et helpers de configuration (.env).

Tâches

- implémenter helpers `load_config()` et `log_request()`
- mesurer et logger durée d'appel LLM
- configurer niveau de log via `LOG_LEVEL`

Critères d'acceptation

- les appels LLM sont loggés avec timestamp et durée
- `LOG_LEVEL` contrôle le niveau de verbosité

Estimate: 0.5 jour
