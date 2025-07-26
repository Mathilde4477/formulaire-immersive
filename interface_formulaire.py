
import streamlit as st
from fpdf import FPDF
import pandas as pd
import os

st.title("Formulaire Immersive - Version Complète")

# Champs d'identité
reference = st.text_input("Référence")
institution = st.text_input("Institution")
titre = st.selectbox("Titre", ["M.", "Mme", "Mlle"])
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
langue = st.selectbox("Langue", ["Français", "Anglais"])
niveau_scolaire = st.text_input("Niveau scolaire")
nombre_personnes = st.number_input("Nombre de personnes", min_value=1, step=1)
capacite_max = st.number_input("Capacité max", min_value=1, step=1)

detail_programme = st.text_area("Champ libre programme")


# Listes bilingues pour le programme
programme_fr = [
    "Plages du Débarquement (secteur US)",
    "Plages du Débarquement (secteur GB)",
    "Plages du Débarquement (secteur Canadien)",
    "Plages du Débarquement (US/GB)",
    "Mont Saint Michel",
    "Vieux Bayeux et Cathédrale",
    "Médiéval",
    "Autre"
]

programme_en = [
    "D-Day beaches (US sector)",
    "D-Day beaches (British sector)",
    "D-Day beaches (Canadian sector)",
    "D-Day beaches (US/GB)",
    "Mont Saint Michel",
    "Old Bayeux and Cathedral",
    "Medieval",
    "Other"
]

# Listes bilingues pour le programme
programme_fr = [
    "Plages du Débarquement (secteur US)",
    "Plages du Débarquement (secteur GB)",
    "Plages du Débarquement (secteur Canadien)",
    "Plages du Débarquement (US/GB)",
    "Mont Saint Michel",
    "Vieux Bayeux et Cathédrale",
    "Médiéval",
    "Autre"
]
programme_fr = [
    "Plages du Débarquement (secteur US)",
    "Plages du Débarquement (secteur GB)",
    "Plages du Débarquement (secteur Canadien)",
    "Plages du Débarquement (US/GB)",
    "Mont Saint Michel",
    "Vieux Bayeux et Cathédrale",
    "Médiéval",
    "Autre"
]
programme_en = [
    "D-Day beaches (US sector)",
    "D-Day beaches (British sector)",
    "D-Day beaches (Canadian sector)",
    "D-Day beaches (US/GB)",
    "Mont Saint Michel",
    "Old Bayeux and Cathedral",
    "Medieval",
    "Other"
]
programme = st.selectbox("Programme", programme_fr if langue_ui == "Français" else programme_en)


# Champs horaires
heure_debut = st.selectbox("Heure de début", [f"{h:02d}:{m:02d}" for h in range(6, 21) for m in range(0, 60, 5)])
lieu_debut = st.text_input("Lieu de début")
heure_fin = st.selectbox("Heure de fin", [f"{h:02d}:{m:02d}" for h in range(6, 22) for m in range(0, 60, 5)])
lieu_fin = st.text_input("Lieu de fin")

# Champs tarifs
type_visite = st.radio("Guide seul ou chauffeur-guide", ["Guide seul", "Chauffeur-guide"])
tarif_guidage = st.number_input("Tarif guidage HT (€)", min_value=0.0, step=1.0, format="%.2f")
tva_guidage = round(tarif_guidage * 0.20, 2)
tarif_chauffeur = st.number_input("Tarif chauffeur HT (€)", min_value=0.0, step=1.0, format="%.2f")
tva_chauffeur = round(tarif_chauffeur * 0.10, 2)
tarif_ttc = round(tarif_guidage + tva_guidage + tarif_chauffeur + tva_chauffeur, 2)

# Durée estimée
from datetime import datetime
try:
    fmt = "%H:%M"
    debut = datetime.strptime(heure_debut, fmt)
    fin = datetime.strptime(heure_fin, fmt)
    duree = str(fin - debut)
except:
    duree = ""

# VIP
vip = st.checkbox("Visite VIP ?")
texte_vip = st.text_area("Informations supplémentaires en cas de VIP") if vip else ""

# Données
ligne = {
    "Référence": reference,
    "Institution": institution,
    "Titre": titre,
    "Nom": nom,
    "Prénom": prenom,
    "Adresse": adresse,
    "Adresse 2": adresse2,
    "Code postal": code_postal,
    "Commune": commune,
    "Pays": pays,
    "Téléphone": telephone,
    "Email": email,
    "Langue": langue,
    "Niveau scolaire": niveau_scolaire,
    "Nombre de personnes": nombre_personnes,
    "Capacité max": capacite_max,
    "Programme": programme,
    "Détail programme": detail_programme,
    "Heure de début": heure_debut,
    "Lieu de début": lieu_debut,
    "Heure de fin": heure_fin,
    "Lieu de fin": lieu_fin,
    "Durée": duree,
    "Type de visite": type_visite,
    "VIP": "Oui" if vip else "Non",
    "Texte VIP": texte_vip,
    "Tarif guidage HT": f"{tarif_guidage:.2f}",
    "TVA guidage (20%)": f"{tva_guidage:.2f}",
    "Tarif chauffeur HT": f"{tarif_chauffeur:.2f}",
    "TVA chauffeur (10%)": f"{tva_chauffeur:.2f}",
    "Tarif TTC": f"{tarif_ttc:.2f}",
    "Nom clients": nom_clients
}

# Export Excel
if st.button("Exporter vers Excel"):
    df = pd.DataFrame([ligne])
    fichier_excel = "formulaire_complet.xlsx"
    df.to_excel(fichier_excel, index=False)
    with open(fichier_excel, "rb") as f:
        st.download_button("Télécharger le fichier Excel", f, fichier_excel)

# Export PDF
if st.button("Générer le PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="Formulaire Immersive - Données complètes")
    for key, value in ligne.items():
        pdf.multi_cell(0, 10, txt=f"{key} : {value}")
    nom_fichier = f"formulaire_{reference or nom}_{institution or prenom}.pdf".replace(" ", "_")
    pdf.output(nom_fichier)
    with open(nom_fichier, "rb") as f:
        st.download_button("Télécharger le PDF", f, nom_fichier, mime="application/pdf")
