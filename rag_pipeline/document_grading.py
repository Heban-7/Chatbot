# Evaluate document relevance
import logging
from rag_pipeline.state_manager import RAGState
from langchain_openai import ChatOpenAI
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def grade_documents(state: RAGState, document_grade: ChatOpenAI) -> RAGState:
    """
    Grades documets based on their relavance to the question
    """
    question = state.get("question")
    documents = state.get("documents", [])

    if not question:
        raise ValueError("question is not founding in the state")
    if not documents:
        logging.info("WARNING: No Documents retrieved")
        return {"documents":[], "question": question}
    
    relevant_docs = []
    for doc in documents:
        score = document_grade.invoke({"queastion": question, "document": doc})
        if score.lower() == "yes":
            logging.info("Document marked as relevant")
            relevant_docs.append(doc)
        else:
            logging.info("Documents filtered out")
    return {"documents": relevant_docs, "question": question}


