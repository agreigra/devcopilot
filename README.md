# DevCopilot — V0

Petit MVP pour démarrer le projet DevCopilot.

Pré-requis

- Python 3.10+

Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Exécution (dev)

```bash
streamlit run app.py
```

Variables d'environnement

- Copier `.env.example` en `.env` et remplir `OPENAI_API_KEY` si vous en avez une.

Notes

- L'implémentation actuelle est minimale; complétez `src/llm_wrapper.py` et `src/utils.py` pour la logique.

run tests

```bash
./.venv/bin/python -m pytest -q src/tests/test_llm_wrapper.py
```
