from ChatBoxSystem.constants import *
from ChatBoxSystem.entity.config_entity import DataIngestionConfig, EmbeddingsConfig, RetrievalConfig
from ChatBoxSystem.utils.helper import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            augmentation=self.params.data_ingestion.augmentation
        )

        return data_ingestion_config
    
    def get_embeddings_config(self) -> EmbeddingsConfig:
        create_directories([self.config.embeddings.root_dir])
        embeddings_config = EmbeddingsConfig(
            root_dir=Path(self.config.embeddings.root_dir),
            embeddings_file=Path(self.config.embeddings.embeddings_file),
            model_name=self.config.embeddings.model_name,
            local_data_file=Path(self.config.embeddings.local_data_file),
        )
        return embeddings_config
    
    def get_retrieval_config(self) -> RetrievalConfig:
        retrieval_config = self.config.retrieval
        retrieval_config = RetrievalConfig(
            top_k=retrieval_config.top_k,
            model_name=self.config.embeddings.model_name,
            embeddings_file=self.config.embeddings.embeddings_file
        )
        return retrieval_config