import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

class CodeIndexer:

    def __init__(self, root_dir: str, index_path: str):
        self.root_dir = root_dir
        self.index_path = index_path
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.documents = []

    def _read_files(self):
        for root, _, files in os.walk(self.root_dir):
            for f in files:
                if f.endswith(".py"):
                    path = os.path.join(root, f)
                    with open(path, "r", encoding="utf-8") as file:
                        self.documents.append((path, file.read()))

    def build(self):
        self._read_files()
        texts = [doc[1] for doc in self.documents]
        embeddings = self.embedder.encode(texts)

        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)

        with open(self.index_path, "wb") as f:
            pickle.dump((index, self.documents), f)
