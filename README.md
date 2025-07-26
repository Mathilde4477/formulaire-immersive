
# Formulaire Immersive Normandy

Ce dépôt contient une application Streamlit permettant de saisir des demandes de visite guidée, générer un fichier Excel et un PDF récapitulatif.

---

## 🚀 Fonctionnalités

- Interface bilingue (français / anglais)
- Sélection de programmes de visite
- Calcul automatique de la TVA
- Calcul de la durée de la visite
- Génération d’un fichier Excel et d’un PDF
- Insertion automatique du logo Immersive Normandy
- Support multiformulaire (plusieurs saisies successives)

---

## 📦 Installation (local)

1. Clonez ce dépôt :
```bash
git clone https://github.com/ton-utilisateur/formulaire-immersive.git
cd formulaire-immersive
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Placez votre logo dans le dossier sous le nom `logo_immersive.png` *(optionnel)*

4. Lancez l'application :
```bash
streamlit run interface_formulaire.py
```

---

## ☁️ Déploiement en ligne

1. Connectez-vous à [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Cliquez sur **"New app"**
3. Sélectionnez ce dépôt GitHub
4. Branche : `main`  
   Fichier principal : `interface_formulaire.py`
5. Cliquez sur **Deploy 🚀**

---

## 📂 Résultats

Les formulaires sont enregistrés dans le dossier `exports/` avec un nom unique incluant la référence et la date.

---

## 🧾 À prévoir

- Fichier PDF : nom personnalisé si institution ou client renseigné
- Champs personnalisables dans Adobe Acrobat si nécessaire

---

## 📧 Contact

Pour toute demande, contactez : `visites@immersive-normandy.com`
