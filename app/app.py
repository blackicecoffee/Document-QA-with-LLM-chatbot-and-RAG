import streamlit as st
from langchain_ollama.llms import OllamaLLM
import chromadb

import asyncio

from chatbot import get_llm_response
from document_extractor import extract_text
from preprocess import text_processing
from vectordb import add_doc, query_doc

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize LLM chatbot
if "llm" not in st.session_state:
    st.session_state.llm = OllamaLLM(model="llama3.2:1b")

# Initialize vector database
if "chroma_collection" not in st.session_state:
    st.session_state.chroma_collection = chromadb.Client().get_or_create_collection(name="docs_collection")

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

st.title("DocQA with LLM and RAG")

with st.sidebar:
    uploaded_files = st.file_uploader(
        label="Choose a file",
        type="pdf",
        accept_multiple_files=True
    )
    if uploaded_files is not None:
        for file in uploaded_files:
            if file not in st.session_state.uploaded_files:
                print(file)
                st.session_state.uploaded_files.append(file)

                file_texts = extract_text(file)
                # print(list(file_texts.values()))

                processed_file_text = text_processing(list(file_texts.values()))
                
                processed_file_text = list(map(lambda x: x.page_content, processed_file_text))

                add_doc(collection=st.session_state.chroma_collection, docs_texts=processed_file_text)

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