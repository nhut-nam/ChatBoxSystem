from ChatBoxSystem.config.configuration import ConfigurationManager
from ChatBoxSystem.generation.generation import Generation
from ChatBoxSystem.retrieval.retrieval import Retrieval

class RAG:
    def __init__(self):
        config = ConfigurationManager()
        retrieval_config = config.get_retrieval_config()
        self.retrieval = Retrieval(retrieval_config)
        self.generation = Generation()

    def answer_query(self, query: str) -> str:
        contexts, distances = self.retrieval.search(query)
        answer = self.generation.generate_answer(query, contexts)
        return answer