from langchain_core.language_models.llms import BaseLLM

from typing import List

from .components.base import BaseRAGComponent

class PreRetriever(BaseRAGComponent):
    def __init__(self, model: BaseLLM):
        self.model = model

    def query_exansion(self, query: str) -> List[str]:
        """Implement Query Expansion Technique"""

        prompt = f"Given this original question: {query}. List three more questions similar and related to this question. Return only the questions, each in a new line with no numbered."

        questions = self.model.invoke(prompt).split("\n")

        return questions

    def generate(self, query):
        expanded_question = self.query_exansion(query=query)

        question_list = [query] + expanded_question

        return question_list