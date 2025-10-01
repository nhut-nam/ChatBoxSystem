from ChatBoxSystem import logger
from ChatBoxSystem.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from ChatBoxSystem.pipeline.stage_02_embeddings import EmbeddingsPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed {e} <<<<<<")

STAGE_NAME = "Embeddings stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EmbeddingsPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed {e} <<<<<<")