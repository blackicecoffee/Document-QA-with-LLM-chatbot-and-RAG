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
        n_results=2
    )

    final_results = ""
    for idx, result in enumerate(results["documents"][0], start=1):
        final_results += f"----- Resource {idx} -----\n{result}\n\n"

    return final_results