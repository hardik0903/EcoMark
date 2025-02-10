import streamlit as st
import subprocess
import os

# List of available apps
APPS = {
    "Energy Analyzer": "energyanalyzer",
    "Sustainable Brands": "sustainablebrands",
    "Sustainable News": "sustainablenews",
    "Sustainable Recommender": "sustainablerecommender",
}

st.title("EcoMark - Sustainable Living Platform")

# Dropdown to select an app
selected_app = st.selectbox("Choose an app:", list(APPS.keys()))

if st.button("Launch App"):
    app_dir = APPS[selected_app]  # Get the folder name
    app_path = os.path.join("External_Apps", app_dir, "Hello.py")

    if os.path.exists(app_path):
        subprocess.run(["streamlit", "run", app_path])
    else:
        st.error(f"Error: {app_path} not found!")
