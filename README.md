# 🤖 RAG-Based AI Chatbot 🔥


A **Retrieval-Augmented Generation (RAG) AI Chatbot** that enhances responses by retrieving relevant documents from an **embedded Pinecone vector database** before generating intelligent answers using LLMs.  

## 🚀 Features  

✅ **FastAPI Backend** for efficient API-based interactions  
✅ **Pinecone Vector Database** for document retrieval  
✅ **LangChain Integration** for structured prompt execution  
✅ **Document Embedding & Storage** (Fetch, Process, Store)  
✅ **Question Rewriting for Better Search Queries**  
✅ **Hallucination & Answer Grading System**  
✅ **Dockerized for Easy Deployment**  

---

## 📂 Project Structure  

```plaintext
rag-chatbot/
│── app/                           # FastAPI application
│   ├── routes/                    # API routes
│   │   ├── rag.py                  # Main RAG API route
│   ├── workflows/                  # Core RAG logic
│   │   ├── nodes.py                 # Document retrieval, grading, generation
│   │   ├── edges.py                 # Workflow decision-making
│   │   ├── graphs.py                # Workflow definition
│   ├── scripts/
│   │   ├── embedding_service.py     # Pinecone embedding & storage
│   ├── dtos/                         # Request & response schemas
│   │   ├── rag.py
│   ├── agent.py                      # LLM & prompt configurations
│── data/                              # Document storage
│── Dockerfile                         # Docker container setup
│── docker-compose.yml                  # Multi-container setup (API + Pinecone)
│── requirements.txt                    # Dependencies
│── .env.example                        # Environment variables template
│── README.md                           # Project documentation
```

--- 

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository

git clone https://github.com/Heban-7/rag-chatbot.git
cd rag-chatbot

### 2️⃣ Set Up Environment Variables

Create a .env file (or rename .env.example) and configure:

```
PINECONE_API_KEY=your_pinecone_api_key
BASE_URI=https://api.openai.com
API_KEY=your_openai_api_key
MODEL_NAME=gpt-4
INDEX_NAME=your_pinecone_index
NAMESPACE=your_pinecone_namespace
```

### 3️⃣ Install Dependencies

```pip install -r requirements.txt```

### 4️⃣ Start the FastAPI Server

```uvicorn app:app --host 0.0.0.0 --port 8000```

## 🐳 Running with Docker

```docker-compose up -d --build```
