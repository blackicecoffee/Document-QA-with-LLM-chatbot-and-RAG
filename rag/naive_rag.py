from langchain_core.language_models.llms import BaseLLM
from chromadb import Collection

class NaiveRAG:
    def __init__(self, model: BaseLLM, vectordb: Collection):
        self.model = model
        self.vectordb = vectordb
        self.pre_retrieval = None
        self.post_retrieval = None

    def retrieval(self, query: str) -> str:
        retrieved_document = self.vectordb.query(
            query_texts=[query],
            n_results=5
        )

        context = ""
        for idx, result in enumerate(retrieved_document["documents"][0], start=1):
            context += f"----- Resource {idx} -----\n{result}\n"

        return context

    async def generate(self, query: str):
        context = self.retrieval(query=query)

        prompt = f"""Instructions: Base on the given context, answer the question of user\nContext:\n{context}\nQuestion: {query}\n"""

        answer = await self.model.ainvoke(prompt)

        return answer
    