# 🤖 Chatbot


## Folder Structure

Chatbot/
│── app.py                    # FastAPI entry point
│── .env                       # Environment variables
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation


├── schemas/                   # Data models for API requests/responses  
│   ├── __init__.py  
│   ├── rag_request.py         # Pydantic model for RAG queries  


├── api/                       # API route handlers  
│   ├── __init__.py  
│   ├── rag_routes.py          # API route for handling RAG queries  


├── rag_pipeline/              # RAG processing logic  
│   ├── __init__.py  
│   ├── graph_builder.py       # Defines the RAG workflow graph  
│   ├── state_manager.py       # RAG state definitions  
│   ├── document_retrieval.py  # Functions for retrieving documents  
│   ├── query_rewriting.py     # Logic for improving user queries  
│   ├── document_grading.py    # Evaluates document relevance  
│   ├── answer_generation.py   # Generates responses from retrieved data  
│   ├── decision_logic.py      # Determines next steps in workflow  
│   ├── prompt_templates.py    # LLM prompt templates  
│   ├── model_wrappers.py      # Wrappers for LLMs and structured outputs  


├── utils/                     # Helper scripts for external services  
│   ├── __init__.py  
│   ├── embedding_manager.py   # Handles vector embeddings with Pinecone  


└── tests/                     # Unit and integration tests  
    ├── __init__.py  
    ├── test_rag_pipeline.py   # Tests for the RAG system  
