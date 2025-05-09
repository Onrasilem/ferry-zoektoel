import streamlit as st
import pandas as pd

# 📥 Excelbestand inlezen
try:
    df = pd.read_excel("Routes.xlsx")
except FileNotFoundError:
    st.error("❌ Het bestand 'routes.xlsx' werd niet gevonden. Zorg dat het in dezelfde map staat als dit script.")
    st.stop()

st.title("🔎 Ferry Route Zoeker")

# 🔍 Invoervelden voor vertrek & bestemming
vertrek = st.text_input("Vertrekhaven (optioneel)").strip()
bestemming = st.text_input("Bestemming (optioneel)").strip()

# 🔽 Dropdown voor rederij
alle_rederijen = ["(Alle rederijen)"] + sorted(df["Rederij"].dropna().unique().tolist())
gekozen_rederij = st.selectbox("Rederij (optioneel)", alle_rederijen)

# 🔎 Filter toepassen
filtered = df.copy()

if vertrek:
    filtered = filtered[filtered["Vertrek"].str.contains(vertrek, case=False, na=False)]

if bestemming:
    filtered = filtered[filtered["Bestemming"].str.contains(bestemming, case=False, na=False)]

if gekozen_rederij != "(Alle rederijen)":
    filtered = filtered[filtered["Rederij"] == gekozen_rederij]

# 📋 Toon resultaten
st.subheader("📄 Zoekresultaten")
if not filtered.empty:
    st.dataframe(filtered.reset_index(drop=True))
else:
    st.info("Geen resultaten gevonden. Probeer andere zoektermen of filter.")
