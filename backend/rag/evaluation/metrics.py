"""
Evaluation metrics for RAG pipeline, including metrics for retriever and generator:
- Relevance: How well does the retrieved context relate to the user's query?
- Faithfulness (or Groundedness): Does the generated answer accurately reflect the information present in the retrieved context?
"""

# ======== RETRIEVER ======== #

def hit_rate():
    pass

def mean_reciprocal_rank():
    pass

def recall_at_k():
    pass

def precision_at_k():
    pass

# ======== GENERATOR ======== #

def llm_as_judge():
    pass
