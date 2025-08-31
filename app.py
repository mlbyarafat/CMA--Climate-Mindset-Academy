import os
import json
from datetime import datetime
import pandas as pd
import plotly.express as px
import streamlit as st

from rag.rag import TinyRAG

st.set_page_config(page_title="Climate Mindset Academy", page_icon="🌍", layout="wide")

# --- Sidebar brand ---
st.sidebar.title("Climate Mindset Academy")
st.sidebar.caption("AI-powered climate learning")

# --- Load seed data ---
@st.cache_data
def load_data():
    co2 = pd.read_csv("data/seed/co2_quarterly_sample.csv", parse_dates=["date"])
    temp = pd.read_csv("data/seed/global_temp_anomaly_sample.csv")
    return co2, temp

co2, temp = load_data()

# --- Load RAG ---
@st.cache_resource
def get_rag():
    return TinyRAG("rag/docs.json")

rag = get_rag()

st.title("Welcome")
st.write(
    "Explore climate data, learn core concepts, and plan actions you can take today. "
    "This deployable prototype runs offline with sample datasets and a simple retrieval system."
)

col1, col2 = st.columns(2)
with col1:
    fig = px.line(co2, x="date", y="co2_ppm", markers=True, title="CO₂ concentration (sample)")
    st.plotly_chart(fig, use_container_width=True)
with col2:
    fig2 = px.bar(temp, x="year", y="temp_anomaly_c", title="Global temperature anomaly (sample)")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("### Ask a question")
q = st.text_input("Type a climate question (e.g., 'What is the greenhouse effect?')")
if st.button("Search facts"):
    hits = rag.search(q or "greenhouse effect", k=3)
    for h in hits:
        with st.expander(f"{h['title']} — relevance {h['score']:.2f}"):
            st.write(h["text"])

st.info("Use the tabs in the left sidebar to open more modules.")

st.sidebar.markdown("---")
st.sidebar.subheader("Modules")
st.sidebar.markdown("Use the *pages/* to navigate modules like **Explore Data**, **Story**, **Action Simulator**, and **Teacher Dashboard**.")
