import streamlit as st
from langchain_ollama.llms import OllamaLLM

import asyncio

from chatbot import get_llm_response

st.title("DocQA with LLM and RAG")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "llm" not in st.session_state:
    st.session_state.llm = OllamaLLM(model="llama3.2:1b")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter something..."):
    # Add user query into chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop=loop)
        
        response = loop.run_until_complete(get_llm_response(llm=st.session_state.llm, prompt=prompt))

        st.markdown(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )