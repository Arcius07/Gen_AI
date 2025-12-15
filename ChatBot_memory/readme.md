# 🤖 Memory-Enabled Gemini Chatbot

A polite, general-purpose AI chatbot built using **LangChain** and **Google Gemini**, enhanced with **conversation memory** to provide contextual and coherent responses.

---

## 🚀 Features

- Uses **Google Gemini (gemini-2.5-flash)** as the LLM
- Supports multiple memory strategies:
  - Conversation Buffer Memory
  - Sliding Window Memory
  - Conversation Summary Memory
- Maintains conversational context across turns
- Clean and modular Python implementation
- Environment-based API key management

---

## 🧠 Memory Types Supported

### 1️⃣ Conversation Buffer Memory
Stores the **entire conversation history**.
Best for short conversations where full context is needed.

### 2️⃣ Conversation Window Memory
Keeps only the **last N interactions**.
Efficient for longer chats with limited context requirements.

### 3️⃣ Conversation Summary Memory
Automatically **summarizes older messages** using the LLM.
Useful for long-running conversations.

---

## 🛠 Tech Stack

- **Python**
- **LangChain**
- **Google Generative AI (Gemini)**
- **dotenv**

---

## 📂 Project Structure

---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-link>
cd memory-gemini-chatbot
```
### 2️⃣ Create Virtual Environment (Optional)
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```
pip install langchain langchain-google-genai python-dotenv
```
### 4️⃣ Set Environment Variables
```
Create a .env file:

GOOGLE_API_KEY=your_google_api_key_here
```
### ▶️ Run the Chatbot
```
python chatbot.py

Type exit or quit to stop the chatbot.
```
