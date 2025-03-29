from fastapi import FastAPI
import uvicorn
from api.rag_routes import rag_router

app = FastAPI(title="SageAI - RAG Chatbot")

# Include the RAG API routes
app.include_router(rag_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
