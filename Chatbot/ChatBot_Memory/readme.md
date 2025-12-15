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

