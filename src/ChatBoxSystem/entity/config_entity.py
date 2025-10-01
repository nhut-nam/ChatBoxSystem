from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str 
    local_data_file: Path
    augmentation: bool
    
@dataclass
class EmbeddingsConfig:
    root_dir: Path
    embeddings_file: Path
    model_name: str
    local_data_file: Path

@dataclass
class RetrievalConfig:
    top_k: int 
    model_name: str
    embeddings_file: str