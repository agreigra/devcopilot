import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="DevCopilot V0")
st.title("DevCopilot — V0")

st.write("Interface MVP — posez une question et recevez une réponse du LLM.")

question = st.text_area("Question", height=150)

if st.button("Envoyer"):
    if not question.strip():
        st.warning("Veuillez saisir une question.")
    else:
        st.info("Envoi au LLM (si configuré)...")
        try:
            # Import local wrapper lazily (sera implémenté dans ticket 02)
            from src.llm_wrapper import LLMWrapper

            wrapper = LLMWrapper()
            response = wrapper.chat([{"role": "user", "content": question}])
            st.success("Réponse :")
            st.markdown(response)
        except Exception as e:
            st.error(f"Erreur lors de l'appel au LLM: {e}")
