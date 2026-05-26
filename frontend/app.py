import requests
import streamlit as st
from loguru import logger

# ✅ logs frontend
logger.add(
    "app.log", format="{time} | {level} | {message}", level="INFO", rotation="1 MB"
)

API_URL = "http://backend:8000/calcul"

st.title("Calcul du carré")

nombre = st.number_input("Entrez un entier", step=1)

if st.button("Calculer"):
    try:
        logger.info(f"Nombre envoyé: {nombre}")

        response = requests.post(API_URL, json={"valeur": int(nombre)})

        if response.status_code == 200:
            resultat = response.json()["resultat"]
            logger.info(f"Résultat reçu: {resultat}")
            st.success(f"Résultat : {resultat}")
        else:
            logger.error(f"Erreur API: {response.status_code}")
            st.error("Erreur API")
    except Exception as e:
        logger.error(f"Erreur frontend: {e}")
        st.error("Erreur de communication avec l'API")
