from langchain_core.language_models.llms import BaseLLM
from chromadb import Collection

class NaiveRAG:
    def __init__(self, model: BaseLLM, vectordb: Collection):
        self.model = model
        self.vectordb = vectordb

    def generate(self, query: str):
        pass
    