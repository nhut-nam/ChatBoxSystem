from ChatBoxSystem.config.configuration import ConfigurationManager 
from ChatBoxSystem.ingestion.data_ingestion import Embeddings
from ChatBoxSystem import logger

STAGE_NAME = "Embeddings stage"

class EmbeddingsPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        embeddings = Embeddings(config=data_ingestion_config)
        embeddings.generate_embeddings()
        logger.info("Embeddings generation completed successfully.")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EmbeddingsPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e