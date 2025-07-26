import streamlit as st
import pandas as pd
from datetime import datetime
import locale

st.set_page_config(page_title="Formulaire de réservation", layout="centered")

st.title("📋 Formulaire de réservation Immersive Normandy")

# Choix de la langue
langue = st.radio("Langue / Language", ["Français", "English"])

# Fonction de traduction
def t(fr, en):
    return fr if langue == "Français" else en

# Données générales
col1, col2 = st.columns(2)
with col1:
    date_demande = st.date_input(t("Date de la demande", "Request date"))
    reference = st.text_input("Référence")
with col2:
    date_visite = st.date_input(t("Date de la visite", "Visit date"))
    institution = st.text_input(t("Institution / Agence", "Institution / Agency"))

nom = st.text_input(t("Nom", "Last name"))
prenom = st.text_input(t("Prénom", "First name"))
adresse = st.text_input(t("Adresse", "Address"))
adresse2 = st.text_input("Adresse 2")
code_postal = st.text_input(t("Code postal", "Zip code"))
ville = st.text_input(t("Commune", "City"))
pays = st.text_input(t("Pays", "Country"))
telephone = st.text_input(t("Téléphone", "Phone"))
email = st.text_input("E-mail")
nb_pers = st.number_input(t("Nombre de personnes", "Number of people"), min_value=1, value=2)
niveau = st.text_input(t("Niveau scolaire (le cas échéant)", "School level (if applicable)"))
langue_visite = st.selectbox(t("Langue de la visite", "Tour language"), ["Français", "Anglais", "Allemand", "Espagnol", "Autre"])

# Programme de la journée
st.markdown("### " + t("Programme de la journée", "Tour program"))

programme = st.selectbox(t("Choisissez un programme", "Select a program"), [
    "Plages du Débarquement - Secteur US",
    "Plages du Débarquement - Secteur US/GB",
    "Plages du Débarquement - Secteur GB",
    "Plages du Débarquement - Secteur Canadien",
    "Mont Saint Michel",
    "Vieux Bayeux & Cathédrale",
    "Médiéval",
    "Autre"
])

description_programme = st.text_area(t("Commentaires ou précisions sur le programme", "Additional notes or description"))

# Visite VIP
st.markdown("### " + t("Option VIP", "VIP option"))
vip = st.checkbox(t("Visite VIP", "VIP tour"))
vip_details = ""
if vip:
    vip_details = st.text_area(t("Informations particulières", "Special instructions"))

# Guide ou chauffeur-guide
st.markdown("### " + t("Type de prestation", "Type of service"))
type_guide = st.radio(t("Choisissez", "Choose"), [t("Guide seul", "Guide only"), t("Chauffeur-guide", "Driver-guide")])

# Tarif
st.markdown("### " + t("Tarifs", "Rates"))
col3, col4 = st.columns(2)
with col3:
    tarif_ht1 = st.number_input(t("Tarif guidage HT", "Guiding net rate"), min_value=0.0, step=0.01)
    tva1 = st.number_input("TVA guidage (%)", value=20 if type_guide == "Chauffeur-guide" else 10)
    st.caption(f"{t('Taux de TVA appliqué pour le guidage', 'Applied VAT rate for guiding')}: {tva1}%")
with col4:
    tarif_ht2 = st.number_input(t("Tarif chauffeur HT", "Driver net rate"), min_value=0.0, step=0.01)
    tva2 = st.number_input("TVA chauffeur (%)", value=10 if type_guide == "Chauffeur-guide" else 0)
    st.caption(f"{t('Taux de TVA appliqué pour le chauffeur', 'Applied VAT rate for driver')}: {tva2}%")

tarif_ttc = round(tarif_ht1 * (1 + tva1 / 100) + tarif_ht2 * (1 + tva2 / 100), 2)

st.success(f"💰 {t('Tarif TTC estimé', 'Estimated total with tax')} : {tarif_ttc:.2f}")

# Export Excel
st.markdown("### " + t("Génération de fichier", "File generation"))

if st.button(t("📄 Générer fichier Excel", "📄 Generate Excel file")):
    infos = {
        "Date de demande": date_demande.strftime("%Y-%m-%d"),
        "Référence": reference,
        "Date de visite": date_visite.strftime("%Y-%m-%d"),
        "Institution": institution,
        "Nom": nom,
        "Prénom": prenom,
        "Adresse": adresse,
        "Adresse 2": adresse2,
        "Code postal": code_postal,
        "Commune": ville,
        "Pays": pays,
        "Téléphone": telephone,
        "Email": email,
        "Nombre de personnes": nb_pers,
        "Niveau scolaire": niveau,
        "Langue de la visite": langue_visite,
        "Programme": programme,
        "Description programme": description_programme,
        "VIP": "Oui" if vip else "Non",
        "Détails VIP": vip_details,
        "Type de prestation": type_guide,
        "Tarif guidage HT": tarif_ht1,
        "TVA guidage": tva1,
        "Tarif chauffeur HT": tarif_ht2,
        "TVA chauffeur": tva2,
        "Tarif TTC": tarif_ttc
    }

    df = pd.DataFrame([infos])
    file_name = "formulaire_nettoye.xlsx"
    df.to_excel(file_name, index=False)
    with open(file_name, "rb") as f:
        st.download_button(label=t("📥 Télécharger le fichier", "📥 Download file"),
                           data=f,
                           file_name=file_name)
