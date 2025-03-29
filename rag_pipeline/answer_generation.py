# Generates response from retrieved documents
from rag_pipeline.state_manager import RAGState
from langchain_openai import ChatOpenAI
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_response(state: RAGState, answer_generator: ChatOpenAI) -> RAGState:
    """
    Generates an answer based on relevant documents.
    """
    logging.info("Generating response...")
    question = state.get("question")
    documents = state.get("documents", [])

    if not question:
        raise ValueError("Question is missing in the state.")

    if not documents:
        logging.info("[WARNING] No relevant documents found. Generating response without context.")
    
    result = answer_generator.invoke({"question": question, "context": documents})

    return {"question": question, "documents": documents, "generation": result}
