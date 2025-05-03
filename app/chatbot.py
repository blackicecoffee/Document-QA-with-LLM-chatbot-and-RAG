from langchain_core.language_models.llms import BaseLLM
import asyncio

async def get_llm_response(llm: BaseLLM, prompt: str) -> str:
    await asyncio.sleep(0)
    response = await llm.ainvoke(prompt)

    return response

if __name__ == "__main__":
    asyncio.run(get_llm_response("Hello"))