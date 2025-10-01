from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from sklearn.preprocessing import normalize


class Retrieval:
    def __init__(self, config: RetrievalConfig):
        self.config = config
        self.model = SentenceTransformer(self.config.model_name)
        self.index = faiss.read_index(self.config.embeddings_file)
        embeddings_file = Path(self.config.embeddings_file)
        self.texts = np.load(embeddings_file.with_suffix('.npy'), allow_pickle=True)

    def search(self, query: str):
        # Implement search logic here
        query_emb = self.model.encode([query], convert_to_numpy=True)
        query_emb = normalize(query_emb)
        distances, indices = self.index.search(query_emb.astype("float32"), self.config.top_k)
        results = [self.texts[i] for i in indices[0]]
        return results, distances