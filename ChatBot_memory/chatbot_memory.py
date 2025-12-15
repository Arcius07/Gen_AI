import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory,
)

from langchain_core.runnables import RunnableSequence

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7,
)


#  Basic Buffer Memory (stores entire conversation)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Sliding Window Memory (keeps only last N messages)
# memory = ConversationBufferWindowMemory(
#     memory_key="chat_history",
#     return_messages=True,
#     k=5    # keep last 5 exchanges
# )

#  Summary Memory (summarizes old messages automatically)
# memory = ConversationSummaryMemory(
#     llm=llm,
#     memory_key="chat_history"
# )

prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template=(
        "You are a polite, helpful, and knowledgeable AI assistant. "
        "Use conversation memory when needed.\n\n"
        "Memory:\n{chat_history}\n\n"
        "User: {user_input}\n"
        "Assistant:"
    )
)

chain = RunnableSequence(
    prompt | llm
)

def chatbot():
    print("🤖 Polite Gemini Assistant (Memory Enabled) | Type 'exit'\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        chat_history = memory.load_memory_variables({})["chat_history"]

        chain_input = {
            "chat_history": chat_history,
            "user_input": user_input
        }

        response = chain.invoke(chain_input)

        print("Assistant:", response.content)
        print("-" * 60)

        memory.save_context(
            {"input": user_input},
            {"output": response.content}
        )


chatbot()
