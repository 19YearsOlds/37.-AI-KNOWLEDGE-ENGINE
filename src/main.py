import os
from src import loaders, preprocess, embedder, vector_store, rag, config

def build_index():
    docs = loaders.load_data_from_folder(config.Data_dir)

    all_chunks, all_embeddings = [], []
    for name, text in docs.items():
        clean = preprocess.clean_text(text)
        chunks = preprocess.chunks_text(clean)
        embeddings = [embedder.get_embeddings(c) for c in chuncks]
        all_chunks.extend(chunks)
        al_embeddings.extend(embeddings)

    vs = vector_store.VectorStore(dim=len(all_embeddings[0]))
    vs.add(all_embeddings, all_chunks)
    vs.save()
    print("Index built and saved.")

def query_engine(question: str):
    vs = vector_store.vectorStore(dim=1536)
    vs.load()

    query_emb = embedder.get_embedding(question)
    context = vs.search(query_emb, k=3)
    answer = rag.generate_answer("\n".join(context), question)
    print("Q:", question)
    print("A:", answer)

if __name__ == "__main__":
    if not os.path.exists(config.INDEX_DIR):
        os.makedirs(config.INDEX_DIR)

    build_index()
    while True:
        q = input("\nAsk me something (or 'exit'): ")
        if q.lower() == "exit":
            break
        query_engine(q)