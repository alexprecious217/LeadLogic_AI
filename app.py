import streamlit as st
from engine import analyze_lead

st.set_page_config(page_title="LeadLogicAI", layout="centered")

st.title("LeadLogic AI Dashboard")
st.write("Professional Sentiment Analysis for Sales Teams")

# The Input Box
user_text = st.text_area("Paste Customer Feedback Here:", height=200,
                         placeholder="Example: I'm frustrated with the current trial...")
if st.button("Analyse Lead"):
    if user_text.strip():
        score, reason = analyze_lead(user_text)
        st.divider()
        st.metric("Lead Priority Score", f"{score}/10")
        st.info(f"**AI Insight:**{reason}")
    else:
        st.warning("Please enter some text first.")