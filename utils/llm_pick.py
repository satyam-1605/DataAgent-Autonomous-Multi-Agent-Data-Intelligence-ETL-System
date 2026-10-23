import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()


def pick_llm(level: str):
    """
    Select an LLM provider based on the required level.

    low    -> Groq
    medium -> Gemini
    high   -> OpenRouter
    """
    level = level.lower().strip()

    if level == "low":
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY"),
        )

    elif level == "medium":
        llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite",
            temperature=0,
            google_api_key=os.getenv("GEMINI_API_KEY"),
        )

    elif level == "high":
        llm = ChatOpenAI(
            model="openrouter/free",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
            temperature=0,
        )

    else:
        raise ValueError(
            f"Unsupported level: {level}. "
            "Use 'low', 'medium', or 'high'."
        )

    return llm


if __name__ == "__main__":
    llm = pick_llm("high")
    response = llm.invoke("What is the capital of France?")
    print(response.content)