import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class CodeRetriever:

    def __init__(self, index_path: str):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        with open(index_path, "rb") as f:
            self.index, self.documents = pickle.load(f)

    def retrieve(self, query: str, k: int = 4):
        q_emb = self.embedder.encode([query])
        _, idxs = self.index.search(np.array(q_emb), k)
        return [self.documents[i] for i in idxs[0]]
