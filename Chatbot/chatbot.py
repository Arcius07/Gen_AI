import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7,
)

prompt = PromptTemplate(
    input_variables=["user_input"],
    template=(
        "You are a polite, helpful, and knowledgeable AI assistant. "
        "Respond clearly and respectfully.\n\n"
        "User: {user_input}\n"
        "Assistant:"
    )
)

def chatbot():
    print("🤖 Polite Gemini Assistant | Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Have a nice day.")
            break

        response = llm.invoke(
            prompt.format(user_input=user_input)
        )

        print("Assistant:", response.content)
        print("---------------------------------------------------")

chatbot()
