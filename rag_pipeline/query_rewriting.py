from rag_pipeline.state_manager import RAGState
from langchain_openai import ChatOpenAI

def transform_query(state: RAGState, question_rewriter: ChatOpenAI) -> RAGState:
    """
    Rewrites the user's query to enhance document retrieval.
    """
    print("[INFO] Rewriting the query...")
    question = state.get("question")

    if not question:
        raise ValueError("Question is missing in the state.")

    refined_question = question_rewriter.invoke({"question": question})

    rewrite_count = state.get("rewrite_count", 0) + 1

    return {"question": refined_question, "rewrite_count": rewrite_count}
