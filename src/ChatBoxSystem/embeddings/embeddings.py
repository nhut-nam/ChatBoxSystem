import pandas as pd
from ChatBoxSystem.entity.config_entity import EmbeddingsConfig
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from ChatBoxSystem import logger

class Embeddings:
    def __init__(self, config: EmbeddingsConfig):
        self.config = config
        self.model = SentenceTransformer(self.config.model_name)

    def generate_embeddings(self):
        logger.info("Loading data...")
        df = pd.read_csv(self.config.local_data_file)
        texts = df['Answer'].tolist()

        logger.info("Generating embeddings...")
        embeddings = self.model.encode(texts, convert_to_tensor=True, show_progress_bar=True)

        self.save_embeddings(embeddings, texts)

    def save_embeddings(self, embeddings, texts):
        logger.info("Saving embeddings...")
        dim = embeddings[0].shape[0]
        index = faiss.IndexFlatL2(dim)

        index.add(np.array(embeddings))
        logger.info(f"Total embeddings indexed: {index.ntotal}")

        faiss.write_index(index, str(self.config.embeddings_file))
        np.save(self.config.embeddings_file.with_suffix('.npy'), np.array(texts))
        logger.info(f"Embeddings saved to {self.config.embeddings_file}")