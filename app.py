# =====================================================
# GEMINI FINANCIAL DECODER
# SmartInternz - Google Cloud Generative AI Project
# =====================================================

# -------------------------------
# 1️⃣ Import Necessary Libraries
# -------------------------------

import os
import re
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI


# -------------------------------
# 2️⃣ Load Environment Variables
# -------------------------------

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("❌ Google API Key not found. Please set GOOGLE_API_KEY in .env file.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)


# -------------------------------
# 3️⃣ Initialize Gemini Model
# -------------------------------

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",   # Updated working model
    temperature=0.3,
    google_api_key=GOOGLE_API_KEY
)


# -------------------------------
# 4️⃣ Prompt Templates
# -------------------------------

templates = {

    "balance_sheet": PromptTemplate(
        input_variables=["data"],
        template="""
You are a professional financial analyst.

Analyze the following Balance Sheet and provide:

- Summary of financial position
- Key assets and liabilities
- Financial strengths and weaknesses
- Investment insights

Balance Sheet Data:
{data}
"""
    ),

    "profit_loss": PromptTemplate(
        input_variables=["data"],
        template="""
You are a financial expert.

Analyze the following Profit & Loss statement and provide:

- Revenue trends
- Expense analysis
- Net profit evaluation
- Business performance insights

Profit & Loss Data:
{data}
"""
    ),

    "cash_flow": PromptTemplate(
        input_variables=["data"],
        template="""
You are a financial consultant.

Analyze the following Cash Flow statement and provide:

- Operating cash flow analysis
- Investing and financing review
- Liquidity position
- Risk factors

Cash Flow Data:
{data}
"""
    )
}


# -------------------------------
# 5️⃣ Helper Functions
# -------------------------------

def read_file(file):
    """Read CSV or TXT file properly"""
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
        return df.to_string()
    else:
        return file.read().decode("utf-8")


def generate_summary(template_key, data):
    prompt = templates[template_key].format(data=data)
    response = llm.invoke(prompt)
    return response


def create_visualization(title, data):
    st.subheader(f"📊 {title}")

    numbers = re.findall(r"\b\d+(?:\.\d+)?\b", data)
    numbers = [float(n) for n in numbers]

    if len(numbers) > 1:
        df = pd.DataFrame({"Values": numbers[:10]})

        st.write("Extracted Numerical Data:")
        st.dataframe(df)

        fig, ax = plt.subplots()
        ax.plot(df["Values"])
        ax.set_title(title)
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")

        st.pyplot(fig)
    else:
        st.info("Not enough numerical data for visualization.")


# -------------------------------
# 6️⃣ File Upload Section
# -------------------------------

def upload_files():
    st.sidebar.header("📂 Upload Financial Documents")

    balance_sheet = st.sidebar.file_uploader(
        "Upload Balance Sheet (CSV or TXT)",
        type=["csv", "txt"]
    )

    profit_loss = st.sidebar.file_uploader(
        "Upload Profit & Loss Statement (CSV or TXT)",
        type=["csv", "txt"]
    )

    cash_flow = st.sidebar.file_uploader(
        "Upload Cash Flow Statement (CSV or TXT)",
        type=["csv", "txt"]
    )

    return balance_sheet, profit_loss, cash_flow


# -------------------------------
# 7️⃣ Streamlit UI
# -------------------------------

st.set_page_config(page_title="Gemini Financial Decoder", layout="wide")

st.title("💰 Gemini Financial Decoder")
st.markdown("### Transforming Complex Financial Data into Actionable Insights")

balance_sheet_file, profit_loss_file, cash_flow_file = upload_files()


# -------------------------------
# 8️⃣ Generate Report Button
# -------------------------------

if st.button("🚀 Generate Financial Reports"):

    with st.spinner("Analyzing financial documents using Gemini AI..."):

        # Balance Sheet
        if balance_sheet_file:
            bs_data = read_file(balance_sheet_file)
            st.header("📘 Balance Sheet Analysis")

            bs_summary = generate_summary("balance_sheet", bs_data)
            st.write(bs_summary)

            create_visualization("Balance Sheet Trends", bs_data)

        # Profit & Loss
        if profit_loss_file:
            pl_data = read_file(profit_loss_file)
            st.header("📗 Profit & Loss Analysis")

            pl_summary = generate_summary("profit_loss", pl_data)
            st.write(pl_summary)

            create_visualization("Profit & Loss Trends", pl_data)

        # Cash Flow
        if cash_flow_file:
            cf_data = read_file(cash_flow_file)
            st.header("📙 Cash Flow Analysis")

            cf_summary = generate_summary("cash_flow", cf_data)
            st.write(cf_summary)

            create_visualization("Cash Flow Trends", cf_data)


st.markdown("---")
st.markdown("Developed using Google Gemini + LangChain + Streamlit")