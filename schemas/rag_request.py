from pydantic import BaseModel, Field

class RAGRequest(BaseModel):
    question: str = Field(description="The query string for the RAG Chatboat")