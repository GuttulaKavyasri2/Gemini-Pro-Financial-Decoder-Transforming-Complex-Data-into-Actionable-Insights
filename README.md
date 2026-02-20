🚀 Gemini Financial Decoder

AI-Powered Financial Statement Analysis System
Built with Streamlit · Google Gemini AI · LangChain · Python

📌 Overview

Gemini Financial Decoder is an intelligent financial analysis web application that transforms raw financial statements into structured, professional insights using Google’s Gemini Generative AI.

The system enables users to upload financial data (Balance Sheet, Profit & Loss, Cash Flow) and receive persona-based AI explanations tailored for:

🧑‍💼 CEO – Strategic Overview

💰 CFO – Detailed Financial Perspective

📈 Investor – ROI & Growth Focus

🏛️ Board Member – Governance Insights

This project demonstrates expertise in:

AI integration

Prompt engineering

Data processing

Interactive dashboards

API-based applications

🎯 Key Features

✨ Upload CSV / Excel financial statements
✨ AI-Generated financial analysis
✨ Persona-based explanations
✨ Financial trend visualizations
✨ Downloadable analysis reports
✨ Secure API key management

🧠 System Architecture
User Upload
     ↓
Data Processing (pandas)
     ↓
Prompt Template (LangChain)
     ↓
Gemini AI (gemini-2.5-flash)
     ↓
AI Financial Insights
     ↓
Visualization + Download Report
🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
Data Processing	pandas
AI Model	Google Gemini (gemini-2.5-flash)
Prompt Engineering	LangChain
Environment Management	python-dotenv
File Handling	openpyxl

📂 Project Structure
Gemini-Financial-Decoder/
│
├── app.py
├── requirements.txt
├── .env              # (Not pushed to GitHub)
├── README.md
└── sample_data/

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/Gemini-Financial-Decoder.git
cd Gemini-Financial-Decoder
2️⃣ Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS/Linux

python -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure API Key

Create a .env file:

GOOGLE_API_KEY="your_api_key_here"

⚠️ Never upload your .env file to GitHub. Add it to .gitignore.

5️⃣ Run the Application
streamlit run app.py
📊 How It Works

Upload financial statement

Select statement type

Choose analysis persona

Click Generate Analysis

View AI-powered insights

Download structured report

📈 Example Use Cases

Business Financial Performance Review

Investment Evaluation

Academic Financial Analysis

Startup Financial Diagnostics

🔍 AI Model Configuration
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are a specialized financial analyst assistant...",
    generation_config={
        "temperature": 0.2,
        "max_output_tokens": 2048
    }
)

🚀 Future Enhancements

Automated Financial Ratio Engine

Multi-language Support

Advanced Data Visualizations

Integration with Live Financial APIs

Python | AI Integration | Prompt Engineering

Data Analysis | Streamlit | API Development

📫 Connect with me:

LinkedIn: (Add link)

GitHub: (Add link)

⭐ Why This Project Stands Out

This project showcases:

Real-world AI application integration

Clean architecture design

Financial domain understanding

Production-ready Streamlit implementation

Secure API handling practices
