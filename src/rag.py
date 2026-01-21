import openai
from src import config

openai.api_key = config.OPENAI_API_KEY

def generate_answer(context, query):
    prompt = f"""
    You are an AI assistant. Use the provided context to answer the question.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """
    response = openai.ChatCompletion.create(
        model=config.LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]