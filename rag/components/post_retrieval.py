from langchain_core.language_models.llms import BaseLLM

from typing import List

from .components.base import BaseRAGComponent

class PostRetriever(BaseRAGComponent):
    def __init__(self, model: BaseLLM):
        self.model = model

    def reranking(self, documents: List[str], top_k: int = 1):
        """Implement re-ranking document"""
        pass

    def generate(self, documents: List[str], top_k: int = 1):
        pass