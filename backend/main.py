import os
import asyncio
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv
# from openai import OpenAI

load_dotenv()

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    messages: list


@app.post("/chat")
async def chat(request: ChatRequest):

    async def stream_generator():
        # stream = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=request.messages,
        #     stream=True,
        # )

        # for chunk in stream:
        #     content = chunk.choices[0].delta.content
        #     if content:
        #         yield content
        #         await asyncio.sleep(0)
        for i in range(30):
            yield str(i)
            time.sleep(1)

    return StreamingResponse(stream_generator(), media_type="text/plain")