import streamlit as st

import joblib, os
# load recommender if available
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "action_recommender.pkl")
def recommend(transport, diet, energy):
    try:
        m = joblib.load(model_path)
        pred = m.predict([[transport,diet,energy]])
        return pred[0]
    except Exception as e:
        return None

import math

st.title("🛠️ Action Simulator")
st.write("Estimate annual CO₂ from daily choices. Numbers are rough, for learning only.")

st.subheader("Daily transport")
km = st.slider("Kilometers traveled per day", 0, 100, 10)
mode = st.selectbox("Mode", ["Car (gasoline)", "Bus", "Metro/Train (electric)", "Bicycle/Walk"])

EF = {
    "Car (gasoline)": 0.192,   # kg CO2 per km (approx)
    "Bus": 0.082,
    "Metro/Train (electric)": 0.045,
    "Bicycle/Walk": 0.0
}

days = 300
annual_kg = km * EF[mode] * days
annual_ton = annual_kg / 1000

st.metric("Estimated annual transport CO₂", f"{annual_ton:.2f} t CO₂e")

st.subheader("Diet shift")
meat_meals = st.slider("Meat-based meals per week", 0, 21, 7)
swap = st.slider("Swap to plant-based meals per week", 0, meat_meals, 3)
# Rough teaching estimate: 1 swapped meal saves ~1.5 kg CO2e
diet_saving = swap * 1.5 * 52 / 1000
st.metric("Estimated diet CO₂ savings", f"{diet_saving:.2f} t CO₂e / year")

total = annual_ton - diet_saving
st.header("Your scenario")
st.write(f"**Approximate total**: {total:.2f} t CO₂e / year (transport minus diet savings).")

st.caption("These numbers are educational estimates. Use local tools/utilities for precise footprints.")
