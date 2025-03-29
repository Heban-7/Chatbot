from fastapi import APIRouter
from schemas.rag_request import RAGRequest
from rag_pipeline.graph_builder import app as rag_workflow

rag_router = APIRouter(prefix='/rag', tags=['RAG'])

@rag_router.post("/query")
async def get_response(request: RAGRequest):
    result = rag_workflow.invoke({"question": request.question})
    return result
