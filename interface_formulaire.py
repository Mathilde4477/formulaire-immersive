
import streamlit as st
from fpdf import FPDF
import pandas as pd
import os

langue_ui = st.selectbox("Choisir la langue / Choose language", ["Français", "English"])
st.title("Formulaire Immersive - Version Complète" if langue_ui == "Français" else "Immersive Form - Full Version")

# Champs d'identité
reference = st.text_input("Référence")
institution = st.text_input("Institution")
titre = st.selectbox("Titre", ["M.", "Mme", "Mlle"] if langue_ui == "Français" else ["Mr", "Mrs", "Ms"])
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
adresse = st.text_input("Adresse")
adresse2 = st.text_input("Adresse 2")
code_postal = st.text_input("Code postal")
commune = st.text_input("Commune")
pays = st.text_input("Pays")
telephone = st.text_input("Téléphone")
email = st.text_input("Email")

nom_clients = st.text_area("Nom des clients")

# Champs visite
langue = st.selectbox("Langue / Language", ["Français", "Anglais"] if langue_ui == "Français" else ["French", "English"])
niveau_scolaire = st.text_input("Niveau scolaire")
nombre_personnes = st.number_input("Nombre de personnes", min_value=1, step=1)
capacite_max = st.number_input("Capacité max", min_value=1, step=1)

programme = st.selectbox("Programme",
    (
        [
            "Plages du Débarquement (secteur US)",
            "Plages du Débarquement (secteur GB)",
            "Plages du Débarquement (secteur Canadien)",
            "Plages du Débarquement (US/GB)",
            "Mont Saint Michel",
            "Vieux Bayeux et Cathédrale",
            "Médiéval",
            "Autre"
        ] if langue_ui == "Français" else [
            "D-Day beaches (US sector)",
            "D-Day beaches (British sector)",
            "D-Day beaches (Canadian sector)",
            "D-Day beaches (US/GB)",
            "Mont Saint Michel",
            "Old Bayeux and Cathedral",
            "Medieval",
            "Other"
        ]
    )
)
