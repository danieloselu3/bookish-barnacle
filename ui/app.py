import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

st.set_page_config(page_title="AI Hackathon Intelligence Agent", layout="wide")

st.title("🧠 AI Hackathon Intelligence Orchestrator")
st.markdown("Enter a query and let the agent gather, analyze, and summarize intelligence data.")

user_prompt = st.text_area("Your Query:", placeholder="e.g., Analyze recent financial activity trends...")

if st.button("Run Analysis"):
    if user_prompt.strip():
        with st.spinner("Analyzing... please wait"):
            res = requests.post(f"{BACKEND_URL}/analyze", json={"prompt": user_prompt})
            if res.status_code == 200:
                st.markdown("### 🧾 Intelligence Report")
                st.write(res.json()["response"])
            else:
                st.error("Backend error: " + res.text)
    else:
        st.warning("Please enter a query.")
