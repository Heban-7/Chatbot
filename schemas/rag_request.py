from pydantic import BaseModel, Field

class RagRequest(BaseModel):
    question: str = Field(description="The query string for the RAG Chatboat")