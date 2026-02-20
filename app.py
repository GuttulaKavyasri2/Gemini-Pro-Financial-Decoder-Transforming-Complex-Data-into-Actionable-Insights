import os
import streamlit as st
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
from google import genai

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

print("Looking for .env at:", env_path)
print("Exists:", env_path.exists())
print("API_KEY:", os.getenv("API_KEY"))

# Page Configuration
st.set_page_config(page_title="Gemini Financial Decoder", page_icon="📊", layout="wide")

# Initialize API Key
api_key = os.environ.get("API_KEY")
if not api_key:
    st.error("API_KEY not found. Please set it in your environment variables or .env file.")
    st.stop()

# Production System Instruction
SYSTEM_INSTRUCTION = """You are a world-class Senior Financial Strategist. 
Transform raw data into strategic intelligence. Focus on accuracy, 
cross-statement analysis, and persona-specific utility."""

# App UI
st.title("🚀 Gemini Pro Financial Decoder")
st.markdown("### Production-Ready Financial Diagnosis Suite")

with st.sidebar:
    st.header("Settings")
    persona = st.selectbox("Perspective Filter", ["Analyst", "Executive", "Journalist"])
    st.info(f"Currently analyzing as: **{persona}**")

def upload_files():
    col1, col2, col3 = st.columns(3)
    with col1:
        bs = st.file_uploader("Balance Sheet", type=["csv", "xlsx"])
    with col2:
        pl = st.file_uploader("Profit & Loss", type=["csv", "xlsx"])
    with col3:
        cf = st.file_uploader("Cash Flow", type=["csv", "xlsx"])
    return bs, pl, cf

def load_data(file):
    if not file: return None
    try:
        return pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
    except Exception as e:
        st.error(f"Error loading {file.name}: {e}")
        return None

bs_file, pl_file, cf_file = upload_files()

if st.button("🚀 INITIATE FULL DIAGNOSIS", type="primary"):
    with st.spinner("Gemini 3 Pro is processing cross-statement diagnostics..."):
        bs_data = load_data(bs_file)
        pl_data = load_data(pl_file)
        cf_data = load_data(cf_file)
        
        if bs_data is None and pl_data is None and cf_data is None:
            st.warning("Please upload at least one financial document.")
            st.stop()

        # Build context
        context = f"PERSONA: {persona}\n"
        if bs_data is not None: context += f"BALANCE_SHEET: {bs_data.to_dict()}\n"
        if pl_data is not None: context += f"PROFIT_LOSS: {pl_data.to_dict()}\n"
        if cf_data is not None: context += f"CASH_FLOW: {cf_data.to_dict()}\n"

        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Analyze these financials and provide a deep summary:\n{context}",
            config={
                "temperature": 0.7,
                "system_instruction": SYSTEM_INSTRUCTION
             }
        )

            st.success("Analysis Complete")
            st.markdown(response.text)

            
            # Visualization Section
            st.divider()
            st.subheader("Data Visualizations")
            v1, v2 = st.columns(2)
            if bs_data is not None:
                with v1: 
                    st.write("**Balance Sheet Trend**")
                    st.line_chart(bs_data.select_dtypes(include=['number']))
            if pl_data is not None:
                with v2:
                    st.write("**Profit & Loss Trend**")
                    st.line_chart(pl_data.select_dtypes(include=['number']))
                    
        except Exception as e:
            st.error(f"Analysis Failed: {str(e)}")