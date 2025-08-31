import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Explore Data")
st.write("Interactive views using the bundled sample datasets. Replace with live sources for production.")

co2 = pd.read_csv("data/seed/co2_quarterly_sample.csv", parse_dates=["date"])
temp = pd.read_csv("data/seed/global_temp_anomaly_sample.csv")

tab1, tab2 = st.tabs(["CO₂", "Temperature"])

with tab1:
    st.write("Quarterly sample of atmospheric CO₂ (ppm).")
    fig = px.line(co2, x="date", y="co2_ppm", markers=True)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(co2)

with tab2:
    st.write("Global mean temperature anomaly (°C) — small sample for demo.")
    fig2 = px.area(temp, x="year", y="temp_anomaly_c")
    st.plotly_chart(fig2, use_container_width=True)
    st.dataframe(temp)
