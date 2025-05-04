from langchain.text_splitter import NLTKTextSplitter, SpacyTextSplitter, CharacterTextSplitter

from typing import List

def text_processing(texts: List[str]) -> List[str]:
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=256,
        chunk_overlap=20
    )
    
    docs = text_splitter.create_documents(texts)
    
    return docs