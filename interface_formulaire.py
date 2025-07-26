import streamlit as st
from fpdf import FPDF
import pandas as pd
import os
import datetime

date_demande = st.date_input("📅 Date de la demande", value=datetime.date.today())
date_visite = st.date_input("📆 Date de la visite")

st.title("Formulaire Immersive - Version Française")

# Puis le reste de ton code...
