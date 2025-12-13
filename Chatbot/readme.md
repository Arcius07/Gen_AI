# 🤖Gemini AI Chatbot (LangChain + Google Generative AI)

A simple command-line AI chatbot built using LangChain and Google’s Gemini model.
The assistant is designed to respond in a polite, helpful, and knowledgeable manner.

# 📌 Features

Uses Google Gemini (gemini-2.5-flash) via langchain-google-genai

Clean and polite conversational behavior

Environment variable support for secure API key handling

Simple CLI interface (terminal-based)

Easily extendable with memory, tools, or RAG

# 🛠️ Tech Stack
```
Python 3.9+

LangChain

Google Generative AI (Gemini)

python-dotenv
```
# 📂 Project Structure
```
.
├── chatbot.py          # Main chatbot script
├── .env                # Environment variables (API key)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
# 🔑 Prerequisites

Python installed (3.9 or above)

A Google Generative AI API key

# ⚙️ Installation

## 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/gemini-politeness-chatbot.git
cd gemini-politeness-chatbot
```
## 2️⃣ Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
# 🔐 Environment Setup
```
Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key_here
```

# ▶️ Running the Chatbot
```
python chatbot.py
```

You’ll see:

🤖 Polite Gemini Assistant | Type 'exit' to quit

# 💬 Example Interaction
```
You: Explain what machine learning is
Assistant: Machine learning is a branch of artificial intelligence that enables
computers to learn from data and improve their performance without being
explicitly programmed.
```

To exit:

You: exit
👋 Goodbye! Have a nice day.

# 🧠 Prompt Design

The assistant follows a system prompt:

"You are a polite, helpful, and knowledgeable AI assistant.
Respond clearly and respectfully."


This ensures:

Professional tone

Clear explanations

User-friendly responses

# 🚀 Possible Improvements

Add conversation memory

Add tool usage (calculator, search, etc.)

Add RAG (PDF / text document support)

Build a Streamlit or FastAPI UI

Logging and conversation history
