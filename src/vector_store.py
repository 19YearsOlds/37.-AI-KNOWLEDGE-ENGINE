import faiss
import numpy as np
import os
import pickle
from src import config

class VectorStore:
    def __init__(self, di, store_path=os.path.join(config.INDEX_DIR, "faiss.index")):
        self.index = faiss.IndexFlatL2(dim)
        self.embeddings = []
        self.text_chunks = []
        self.store_path = store_path

    def add(self, embeddings, texts):
        embbeddings = np.array(embeddings).astype("float32")
        self.index.add(embeddings)
        self.embeddings.extend(embeddings)
        self.text_chunks.extend(texts)

    def search(self, query_embedding, k=3):
        query = np.array([query_embediing]).astype("float32")
        distances, indices = self.index.search(query, k)
        return [self.text_chunks[i] for i in indices[0]]
    
    def save(self):
        faiss.write_index(self.index, self.store_path)
        with open(self.store_path + ".meta", "wb") as f:
            pickle.dump(self.text_chunks, f)

    def load(self):
        self.index = faiss.read_index(self.store_path)
        with open(self.store_path + ".meta", "rb") as f:
            self.text_chunks = pickle.load(f)