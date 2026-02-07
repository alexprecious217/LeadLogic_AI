import google.generativeai as genai
import streamlit as st

#Securely fetch the API key from Streamlit's secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception:
    st.error("API Key is missing. Please add it to Streamlit Secrets.")

def analyze_lead(text):
    """
    Core AI logic: Categorizes text sentiment into business actions.
    """
    prompt = f"""
    You are an expert sales lead analyst. Analyze this message: "{text}"
    and return ONLY a 1 - 10 score and a 1 - sentence business recommendation.
    Return your answer in this EXACT format:
        Score: [number]
        Reson: [sentence]
    """
    try:
        response = model.generate_content(prompt)
        result = response.text.split('\n')
        score = result[0].replace('Score: ', '').strip()
        reason = result[1].replace('Reason: ', '').strip()
        return float(score), reason
    except:
        return 5.0, "AI Engine temporarily unavailable."

