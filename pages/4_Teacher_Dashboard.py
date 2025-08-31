import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Teacher Dashboard (Lite)")
st.write("Create a class code, collect student pledges, and export progress.")

if "pledges" not in st.session_state:
    st.session_state.pledges = []

col1, col2 = st.columns([2,1])
with col1:
    name = st.text_input("Student name")
    action = st.text_input("Action pledge (e.g., 'Cycle to school twice a week')")
    if st.button("Add pledge"):
        if name and action:
            st.session_state.pledges.append({"name": name, "action": action})
            st.success("Recorded")
        else:
            st.warning("Please enter both fields.")

with col2:
    st.metric("Pledges recorded", len(st.session_state.pledges))

st.subheader("Pledges")
df = pd.DataFrame(st.session_state.pledges) if st.session_state.pledges else pd.DataFrame(columns=["name","action"])
st.dataframe(df, use_container_width=True)

st.download_button("Export CSV", df.to_csv(index=False).encode("utf-8"), "class_pledges.csv", "text/csv")
