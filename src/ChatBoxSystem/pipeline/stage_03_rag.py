from ChatBoxSystem.RAG import RAG
from ChatBoxSystem import config, logger

STAGE_NAME = "Embeddings stage"

class EmbeddingsPipeline:
    def __init__(self):
        pass

    def main(self):
        rag = RAG()
        print(rag.answer_query("What is your name?"))
        logger.info("Embeddings generation completed successfully.")

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EmbeddingsPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e