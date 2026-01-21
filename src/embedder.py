import openai
from src import config

openai.api_key = config.OPENAI_API_KEY

def get_embedding(text: str):
    response = openai.Embedding.create(
        input=text,
        model=config.EMBEDDING_MODEL
    )
    return response["data"][0]["embedding"]