import os

DATA_DIR = os.path.join(os.getcwd(),"data")
INDEX_DIR = os.path.join(os.getcwd(), "outputs")

EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-4o-mini"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")