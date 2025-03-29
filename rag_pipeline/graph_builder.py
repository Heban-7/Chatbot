import os
from dotenv import load_dotenv, find_dotenv
from rag_pipeline.document_retrieval import retrieve_documents
from rag_pipeline.query_rewriting import transform_query
from rag_pipeline.document_grading import grade_documents
from rag_pipeline.answer_generation import generate_response
from rag_pipeline.decision_logic import decide_to_generate
from rag_pipeline.state_manager import RAGState
from utils.embedding_manager import PineconeEmbeddingManager
from langgraph.graph import START, END, StateGraph

# Load environment variables
load_dotenv(find_dotenv())
api_key = os.environ.get('PINECONE_API_KEY')
index_name = os.environ.get('INDEX_NAME')
name_space = os.environ.get('NAMESPACE')

# Instantiate Pinecone manager
manager = PineconeEmbeddingManager(api_key=api_key, index_name=index_name, name_space=name_space)

# Define the graph nodes
retriever = lambda state: retrieve_documents(state=state, retriever=manager)    
grader = lambda state: grade_documents(state=state)
rewriter = lambda state: transform_query(state=state)
generator = lambda state: generate_response(state=state)

# Create workflow graph
workflow = StateGraph(RAGState)
workflow.add_node("retrieve", retriever)
workflow.add_node("rewriter", rewriter)
workflow.add_node("grade_documents", grader)
workflow.add_node("answer_generator", generator)

# Define edges
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_edge("rewriter", "retrieve")
workflow.add_edge("answer_generator", END)

# Conditional edges
workflow.add_conditional_edges(source="grade_documents", path=decide_to_generate)

# Compile workflow
app = workflow.compile()
