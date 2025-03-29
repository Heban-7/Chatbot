# Determine next steps in workflow
from rag_pipeline.state_manager import RAGState
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def decide_to_generate(state: RAGState, max_rewrites: int = 2) -> str:
    """
    Determines whether to generate an answer or refine the query.
    """
    logging.info("Evaluating retrieved documents for answer generation...")
    documents = state.get("documents", [])
    rewrite_count = state.get("rewrite_count", 0)

    if not documents:
        if rewrite_count >= max_rewrites:
            logging.info("Max rewrites reached. Proceeding with answer generation.")
            return "answer_generator"
        else:
            logging.info("[No relevant documents. Rewriting query...")
            return "rewriter"
    else:
        logging.info("Sufficient documents found. Proceeding with answer generation.")
        return "answer_generator"
