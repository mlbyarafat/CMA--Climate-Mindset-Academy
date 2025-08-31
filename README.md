# Climate Mindset Academy — Deployable Prototype

Interactive, AI-aided climate education app built with Streamlit. This bundle runs offline
with sample datasets and a tiny retrieval system, and is ready to deploy on Streamlit Community Cloud or Docker.

## Features
- 📊 Explore CO₂ and temperature anomaly sample datasets
- 📖 Story module with explainers (backed by a tiny local RAG)
- 🛠️ Action simulator for personal choices
- 👩‍🏫 Lite teacher dashboard with CSV export
- 🌐 Multiplatform: local, Streamlit Cloud, Docker

## Quickstart (local)
```bash
pip install -r requirements.txt
streamlit run app.py
```
App URL: http://localhost:8501

## Deploy: Streamlit Community Cloud
1. Push this folder to a public Git repo.
2. On https://share.streamlit.io, create a new app pointing to `app.py` (Python 3.11).
3. Add the following (optional) secrets if you later integrate external APIs:
   - `OPENAI_API_KEY` (not required for this prototype).
4. Click **Deploy**.

## Deploy: Docker
```bash
docker build -t climate-mindset-academy .
docker run -p 8501:8501 climate-mindset-academy
```
Open http://localhost:8501

## Project structure
```
.
├─ app.py
├─ pages/
│  ├─ 1_Explore_Data.py
│  ├─ 2_Story_Module.py
│  ├─ 3_Action_Simulator.py
│  └─ 4_Teacher_Dashboard.py
├─ data/seed/
│  ├─ co2_quarterly_sample.csv
│  └─ global_temp_anomaly_sample.csv
├─ rag/
│  ├─ docs.json
│  └─ rag.py
├─ .streamlit/config.toml
├─ requirements.txt
└─ Dockerfile
```

## Notes
- Replace the **sample datasets** with trusted sources (NASA/NOAA/Met) and add timestamps & citations in the UI.
- The current RAG uses a tiny TF/cosine approach over `rag/docs.json` for offline use; swap in a vector DB + model for production.
- All numbers in the simulator are **educational estimates**.


## Small onboard ML model
- A tiny synthetic-trained recommender (`models/action_recommender.pkl`) provides personalized *action suggestions* in the Action Simulator. It's trained on synthetic data for demo purposes; replace with real user data and retrain for production.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
