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
        category, action, score = analyze_lead(user_text)
        st.divider()
        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="lead Category", value=category)
            st.write(f"**AI Confidence Score:** {score:.2f}")

        with col2:
            st.subheader("Recommended Action")
            st.success(action)
    else:
        st.warning("Please enter some text for the AI to analyze.")
        