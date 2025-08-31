import streamlit as st
from rag.rag import TinyRAG

st.title("Story Module: The Greenhouse Effect")
st.write("A short, guided walkthrough with embedded explanations.")

rag = TinyRAG("rag/docs.json")
facts = rag.search("greenhouse effect", k=1)
st.image("https://upload.wikimedia.org/wikipedia/commons/5/5c/Greenhouse_Effect.svg", caption="Schematic of the greenhouse effect")

st.markdown("""
**Scene 1: Sunlight Arrives**  
Sunlight warms Earth's surface. Some energy is reflected; some becomes heat.

**Scene 2: Heat Tries to Leave**  
Earth emits infrared radiation back toward space.

**Scene 3: Greenhouse Gases Trap Heat**  
Gases like CO₂ and CH₄ absorb and re-emit some of this heat, keeping the lower atmosphere warmer.

**Scene 4: Human Influence**  
Burning fossil fuels increases greenhouse gases, strengthening the effect.
""")

if facts:
    with st.expander("Read more"):
        st.write(facts[0]["text"])

st.success("Takeaway: The greenhouse effect is natural; adding more greenhouse gases increases warming.")
