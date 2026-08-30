# Ticket 05 — Tests unitaires pour V0

Description

- Ajouter tests unitaires pour `LLMWrapper` et composants critiques.

Tâches

- écrire `src/tests/test_llm_wrapper.py` (mock path + provider error)
- écrire `src/tests/test_app.py` (test fonctions de présentation / logique séparée de Streamlit)
- configurer `pytest` minimal

Critères d'acceptation

- `pytest` passe pour les tests ajoutés en environnement sans clé LLM
- les tests couvrent les cas mock et erreur provider

Estimate: 1 jour
