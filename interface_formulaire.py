import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Formulaire Immersive Normandy", page_icon="📋")

st.title("📋 Formulaire de réservation")
st.write("Saisissez les informations du formulaire à générer.")

# Champs de saisie
col1, col2 = st.columns(2)

with col1:
    date_demande = st.date_input("Date de la demande", value=datetime.today())
    reference = st.text_input("Référence", value="REF123")
    date_visite = st.date_input("Date de la visite")
    institution = st.text_input("Institution")
    titre = st.selectbox("Titre", ["Monsieur", "Madame", ""])
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")

with col2:
    adresse = st.text_input("Adresse")
    adresse2 = st.text_input("Adresse (suite)")
    code_postal = st.text_input("Code postal")
    commune = st.text_input("Commune")
    pays = st.text_input("Pays")
    tel = st.text_input("Téléphone")
    mail = st.text_input("E-mail")

nb_pers = st.number_input("Nombre de personnes", min_value=1, step=1)
niveau = st.text_input("Niveau scolaire")
langue = st.selectbox("Langue", ["Français", "Anglais", "Autre"])
capacite = st.number_input("Capacité max", min_value=1, step=1)

nom_clients = st.text_input("Nom du groupe / clients")
h_debut = st.text_input("Heure début", value="10h00")
lieu_debut = st.text_input("Lieu début")
h_fin = st.text_input("Heure fin", value="18h00")
lieu_fin = st.text_input("Lieu fin")
duree = st.text_input("Durée", value="8h00")

col3, col4, col5 = st.columns(3)
with col3:
    tarif_ht = st.number_input("Tarif HT", step=1.0)
with col4:
    tva = st.number_input("TVA", step=1.0)
with col5:
    tarif_ttc = st.number_input("Tarif TTC", step=1.0)

# Enregistrement dans un fichier Excel à une ligne
if st.button("📄 Générer fichier Excel"):
    df = pd.DataFrame([{
        "DATE DEMANDE": date_demande.strftime("%d/%m/%Y"),
        "REFERENCE": reference,
        "DATE": date_visite.strftime("%d/%m/%Y"),
        "demande": institution,
        "INSTITUTION": institution,
        "TITRE": titre,
        "NOM": nom,
        "PRENOM": prenom,
        "ADRESSE": adresse,
        "ADRESSE 2": adresse2,
        "CODE POSTALE": code_postal,
        "COMMUNE": commune,
        "PAYS": pays,
        "TEL": tel,
        "MAIL": mail,
        "Nombre de personnes": nb_pers,
        "niveau scolaire": niveau,
        "Langue": langue,
        "Capacité max": capacite,
        "NOM CLIENTS": nom_clients,
        "H DEBUT": h_debut,
        "LIEU DEBUT": lieu_debut,
        "H FIN": h_fin,
        "LIEU FIN": lieu_fin,
        "Durée": duree,
        "tarif ht": tarif_ht,
        "tva": tva,
        "tarif TTC": tarif_ttc
    }])

    output_file = "formulaire_nettoye.xlsx"
    df.to_excel(output_file, index=False)
    st.success(f"✅ Fichier '{output_file}' généré avec succès.")
    with open(output_file, "rb") as f:
        st.download_button("⬇️ Télécharger le fichier Excel", f, file_name=output_file)

