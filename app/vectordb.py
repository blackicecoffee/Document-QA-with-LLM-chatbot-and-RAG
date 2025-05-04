from chromadb import Collection

def add_doc(collection: Collection, docs_texts: list[str]):
    num_chunks = collection.count()

    collection.add(
        documents=docs_texts,
        ids=[f"id{num_chunks + idx}" for idx in range(len(docs_texts))]
    )

def query_doc(collection: Collection, text: str):
    results = collection.query(
        query_texts=[text],
        n_results=1
    )

    return results["documents"][0][0]