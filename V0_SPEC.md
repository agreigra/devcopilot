# V0 — Cahier des charges minimal (DevCopilot)

Objectif V0 : produire un MVP fonctionnel permettant à un utilisateur de poser une question via une UI Streamlit, d'appeler un wrapper LLM provider-agnostique et d'afficher la réponse. Favoriser testabilité et séparation UI / logique.

1. Cahier des charges minimal

- UI Streamlit simple : champ texte, bouton envoyer, zone d'affichage réponse.
- Wrapper LLM (`llm_wrapper.py`) abstrait le provider (méthode `chat(messages) -> str`).
- Logging basique des requêtes (timestamp, durée, tokens estimés).
- Tests unitaires :
  - `test_llm_wrapper.py` (mock LLM) : vérifie que `chat` est appelé et gère erreur.
  - `test_app.py` (appel partiel avec client Streamlit ou test de fonction de présentation).

2. Arborescence proposée

devcopilot/

- app.py # Streamlit entrypoint
- requirements.txt
- .env.example
- README.md
- src/
  - llm_wrapper.py # wrapper provider-agnostique
  - tools/
    - mock_tools.py # implementations simulées pour V1 (optionnel)
  - utils.py # logging, config helpers
  - tests/
    - test_llm_wrapper.py
    - test_app.py

3. Dépendances nécessaires (V0)

- streamlit
- openai (ou SDK du provider choisi) # pour wrapper LLM
- python-dotenv # charger .env en dev
- pytest
- requests
- pydantic # validation simple des outputs (optionnel)

Exemple pour `requirements.txt`:
streamlit
openai
python-dotenv
pytest
requests
pydantic

4. Variables d'environnement nécessaires

- `OPENAI_API_KEY` (ou `LLM_API_KEY`) — clé pour provider LLM
- `LLM_PROVIDER` — ex: "openai" (permet d'abstraire plusieurs providers)
- `LOG_LEVEL` — ex: INFO

5. Étapes d'implémentation (ordre recommandé)

1) Créer un environnement virtuel et `requirements.txt`.
2) Implémenter `src/llm_wrapper.py` avec une implémentation minimale qui appelle l'API (ou un mock local si pas de clé).
3) Écrire `app.py` (Streamlit) : champ question → appelle `llm_wrapper.chat()` → affiche réponse.
4) Ajouter logging simple dans `utils.py` (durée, erreurs).
5) Écrire tests unitaires pour le wrapper (mock) et pour l'app (fonctionalités critiques).
6) Itérer : améliorer gestion d'erreurs, timeouts, configuration via env.

6. Premier exercice à coder (concret et limité)

- Tâche : implémenter `src/llm_wrapper.py` avec une classe `LLMWrapper` et une méthode `chat(messages: List[dict]) -> str`.
- Contraintes :
  - Exposer une implémentation qui, si `OPENAI_API_KEY` absent, retourne une réponse simulée (mock) pour faciliter les tests.
  - Ajouter 2 tests :
    1. test que `chat` renvoie une string quand la clé est absente (mock path).
    2. test que `chat` lève une exception contrôlée en cas de réponse invalide du provider.

---

Si vous voulez, je peux créer automatiquement les fichiers de squelette (`app.py`, `src/llm_wrapper.py`, `src/utils.py`, `requirements.txt`, `.env.example`, tests) et implémenter `LLMWrapper` mock + tests. Souhaitez-vous que je le fasse ?
