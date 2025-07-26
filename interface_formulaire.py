from fpdf import FPDF
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Formulaire de réservation", layout="centered")

st.title("📋 Formulaire de réservation Immersive Normandy")


def select_time(label):
    times = [f"{h:02}:{m:02}" for h in range(24) for m in range(0, 60, 5)]
    return st.selectbox(label, times)






langue = st.radio("Langue / Language", ["Français", "English"])

def t(fr, en):
    return fr if langue == "Français" else en

# Infos principales
col1, col2 = st.columns(2)
with col1:
    date_demande = st.date_input(t("Date de la demande", "Request date"))
    reference = st.text_input("Référence")
with col2:
    date_visite = st.date_input(t("Date de la visite", "Visit date"))
    institution = st.text_input(t("Institution / Agence", "Institution / Agency"))

# Coordonnées client
titre_options_fr = ["", "M.", "Mme", "Mlle"]
titre_options_en = ["", "Mr", "Mrs", "Miss"]
titre = st.selectbox(t("Titre", "Title"), titre_options_fr if langue == "Français" else titre_options_en)
nom = st.text_input(t("Nom", "Last name"))
prenom = st.text_input(t("Prénom", "First name"))
adresse = st.text_input(t("Adresse", "Address"))
adresse2 = st.text_input("Adresse 2")
code_postal = st.text_input(t("Code postal", "Zip code"))
ville = st.text_input(t("Commune", "City"))
pays = st.text_input(t("Pays", "Country"))
telephone = st.text_input(t("Téléphone", "Phone"))
email = st.text_input("E-mail")
nom_client = st.text_input(t("Nom du client", "Client name"))
nb_pers = st.number_input(t("Nombre de personnes", "Number of people"), min_value=1, value=2)
niveau = st.text_input(t("Niveau scolaire (le cas échéant)", "School level (if applicable)"))
capacite_max = st.number_input(t("Capacité max de visite", "Max group capacity"), min_value=1, value=30)
langue_visite = st.selectbox(t("Langue de la visite", "Tour language"), ["Français", "Anglais", "Allemand", "Espagnol", "Autre"] if langue == "Français" else ["French", "English", "German", "Spanish", "Other"])

# Programme
st.markdown("### " + t("Programme de la journée", "Tour program"))
programmes_fr = [
    "Plages du Débarquement - Secteur US",
    "Plages du Débarquement - Secteur US/GB",
    "Plages du Débarquement - Secteur GB",
    "Plages du Débarquement - Secteur Canadien",
    "Mont Saint Michel",
    "Vieux Bayeux & Cathédrale",
    "Médiéval",
    "Autre"
]
programmes_en = [
    "D-Day Beaches - US Sector",
    "D-Day Beaches - US/UK Sector",
    "D-Day Beaches - UK Sector",
    "D-Day Beaches - Canadian Sector",
    "Mont Saint Michel",
    "Old Bayeux & Cathedral",
    "Medieval",
    "Other"
]
programme = st.selectbox(t("Choisissez un programme", "Select a program"), programmes_fr if langue == "Français" else programmes_en)
description_programme = st.text_area(t("Commentaires ou précisions sur le programme", "Additional notes or description"))

# Horaires
st.markdown("### " + t("Horaires de la visite", "Tour schedule"))

col3, col4 = st.columns(2)
with col3:
    h_debut = select_time(t("Heure de début", "Start time"))
    lieu_debut = st.text_input(t("Lieu de début", "Start location"))
with col4:
    h_fin = select_time(t("Heure de fin", "End time"))
    lieu_fin = st.text_input(t("Lieu de fin", "End location"))

# Calcul de durée
try:
    fmt = "%H:%M"
    h1 = datetime.strptime(h_debut.strip(), fmt)
    h2 = datetime.strptime(h_fin.strip(), fmt)
    delta = (h2 - h1).seconds / 3600
    duree = round(delta, 2)
    st.info(f"⏱️ {t('Durée estimée', 'Estimated duration')}: {duree} heures")
except:
    duree = ""
    st.warning(t("Durée non calculable – format attendu HH:MM", "Duration could not be calculated – expected format HH:MM"))


# Option VIP
st.markdown("### " + t("Option VIP", "VIP option"))
vip = st.checkbox(t("Visite VIP", "VIP tour"))
vip_details = ""
if vip:
    vip_details = st.text_area(t("Informations particulières", "Special instructions"))

# Guide ou chauffeur-guide
st.markdown("### " + t("Type de prestation", "Type of service"))
type_guide = st.radio(t("Choisissez", "Choose"), [t("Guide seul", "Guide only"), t("Chauffeur-guide", "Driver-guide")])

# Tarifs avec TVA automatiques
st.markdown("### " + t("Tarifs", "Rates"))
col5, col6 = st.columns(2)
with col5:
    tarif_ht1 = st.number_input(t("Tarif guidage HT", "Guiding net rate"), min_value=0.0, step=0.01)
    tva1 = 20.0
    montant_tva1 = round(tarif_ht1 * tva1 / 100, 2)
    st.caption(f"{t('Taux de TVA appliqué pour le guidage', 'Applied VAT rate for guiding')}: {tva1}%")
    st.text_input("Montant TVA guidage", value=f"{montant_tva1:.2f}", disabled=True)
with col6:
    tarif_ht2 = st.number_input(t("Tarif chauffeur HT", "Driver net rate"), min_value=0.0, step=0.01)
    tva2 = 10.0
    montant_tva2 = round(tarif_ht2 * tva2 / 100, 2)
    st.caption(f"{t('Taux de TVA appliqué pour le chauffeur', 'Applied VAT rate for driver')}: {tva2}%")
    st.text_input("Montant TVA chauffeur", value=f"{montant_tva2:.2f}", disabled=True)

tarif_ttc = round(tarif_ht1 + montant_tva1 + tarif_ht2 + montant_tva2, 2)
st.success(f"💰 {t('Tarif TTC estimé', 'Estimated total with tax')} : {tarif_ttc:.2f}")

# Export Excel
st.markdown("### " + t("Génération de fichier", "File generation"))

if st.button(t("📄 Générer fichier Excel", "📄 Generate Excel file")):
    # Création d’un PDF de confirmation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
# Ajout du logo Immersive Normandy
    logo_path = "logo_immersive.png"
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=10, y=8, w=40)
        pdf.ln(25)

    pdf.cell(200, 10, txt="Récapitulatif de la demande Immersive Normandy", ln=True, align='C')
    pdf.ln(10)

    for key, value in infos.items():
        pdf.multi_cell(0, 10, txt=f"{key} : {value}")

    # Nom de base du fichier PDF selon les informations
    nom_base = reference
    if institution:
        nom_base += f"_{institution.replace(' ', '_')}"
    elif nom and prenom:
        nom_base += f"_{nom.replace(' ', '_')}_{prenom.replace(' ', '_')}"

    pdf_file = os.path.join(export_dir, f"{nom_base}_{horodatage}.pdf")
    pdf.output(pdf_file)
    st.success("✅ " + t("Formulaire sauvegardé", "Form successfully saved"))
    st.toast(t("Formulaire prêt pour une nouvelle saisie", "Ready for a new entry"))
    st.experimental_rerun()
    infos = {
        "Date de demande": date_demande.strftime("%Y-%m-%d"),
        "Référence": reference,
        "Date de visite": date_visite.strftime("%Y-%m-%d"),
        "Institution": institution,
        "Titre": titre,
        "Nom": nom,
        "Prénom": prenom,
        "Adresse": adresse,
        "Adresse 2": adresse2,
        "Code postal": code_postal,
        "Commune": ville,
        "Pays": pays,
        "Téléphone": telephone,
        "Email": email,
        "Nom client": nom_client,
        "Nombre de personnes": nb_pers,
        "Niveau scolaire": niveau,
        "Langue de la visite": langue_visite,
        "Capacité max": capacite_max,
        "Programme": programme,
        "Description programme": description_programme,
        "Heure début": h_debut,
        "Lieu début": lieu_debut,
        "Heure fin": h_fin,
        "Lieu fin": lieu_fin,
        "VIP": "Oui" if vip else "Non",
        "Détails VIP": vip_details,
        "Type de prestation": type_guide,
        "Tarif guidage HT": tarif_ht1,
        "Taux TVA guidage (%)": tva1,
        "Montant TVA guidage": montant_tva1,
        "Tarif chauffeur HT": tarif_ht2,
        "Taux TVA chauffeur (%)": tva2,
        "Montant TVA chauffeur": montant_tva2,
        "Durée estimée (h)": duree,
        "Tarif TTC": tarif_ttc
    }

    df = pd.DataFrame([infos])
    # Création du dossier export si nécessaire
    export_dir = "exports"
    os.makedirs(export_dir, exist_ok=True)

    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(export_dir, f"formulaire_nettoye_{horodatage}.xlsx")
    df.to_excel(file_name, index=False)
    with open(file_name, "rb") as f:
        st.download_button(label=t("📥 Télécharger le fichier", "📥 Download file"),
                           data=f,
                           file_name=file_name)
