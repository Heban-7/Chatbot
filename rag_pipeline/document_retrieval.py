# Function to retrieve documents

from utils.embedding_manager import PineconeEmbeddingManager
from rag_pipeline.state_manager import RAGState


def retrieve_documents(state:RAGState, retriever: PineconeEmbeddingManager) -> RAGState:
    """
    Retrive relevant document based on the input query using pinecone vector search
    """
    question = state.get("question")
    if not question:
        raise ValueError("Question is missing in the state")
    
    documents = retriever.search_matching(query=question)
    return {"question": question, "documents": documents}
