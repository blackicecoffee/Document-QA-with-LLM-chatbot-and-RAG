from .components.base import BaseRAGComponent

class PostRetriever(BaseRAGComponent):
    def __init__(self):
        super().__init__()

    def generate(self, query):
        return super().generate(query)