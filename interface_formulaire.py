
import streamlit as st
from fpdf import FPDF
import pandas as pd
import os

st.title("Formulaire Immersive - Test Fonctionnel")

# Champs de base
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
email = st.text_input("Email")

# Création d'une ligne de données
ligne = {
    "Nom": nom,
    "Prénom": prenom,
    "Email": email
}

# Export Excel
if st.button("Exporter vers Excel"):
    df = pd.DataFrame([ligne])
    fichier_excel = "formulaire_export.xlsx"
    df.to_excel(fichier_excel, index=False)
    with open(fichier_excel, "rb") as f:
        st.download_button("Télécharger le fichier Excel", f, fichier_excel)

# Export PDF
if st.button("Générer le PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="Formulaire Immersive - Données")
    pdf.multi_cell(0, 10, txt=f"Nom : {nom}")
    pdf.multi_cell(0, 10, txt=f"Prénom : {prenom}")
    pdf.multi_cell(0, 10, txt=f"Email : {email}")
    nom_fichier = f"formulaire_{nom}_{prenom}.pdf".replace(" ", "_")
    pdf.output(nom_fichier)
    with open(nom_fichier, "rb") as f:
        st.download_button("Télécharger le PDF", f, nom_fichier, mime="application/pdf")
