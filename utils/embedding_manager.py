import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
# Load environment variables
load_dotenv(find_dotenv())

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
OPENAI_API_KEY=os.getenv("API_KEY")

class PineconeEmbeddingManager:
    """
    Manages embedding-based document retrieval using Pinecone.
    """
    def __init__(self, api_key: str, index_name: str, name_space: str):
        pinecone.init(api_key=api_key)
        self.index = pinecone.Index(index_name)
        self.name_space = name_space

    def search_matching(self, query: str, top_k: int = 5):
        """
        Searches for documents in Pinecone based on query embeddings.
        """
        print("[INFO] Performing vector search in Pinecone...")
        vector = self._embed_query(query)
        results = self.index.query(vector, top_k=top_k, namespace=self.name_space, include_metadata=True)
        return [match["metadata"]["text"] for match in results["matches"]] if results["matches"] else []

    def _embed_query(self, query: str):
        """
        Converts query text to an embedding vector.
        """
        embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL, openai_api_key=OPENAI_API_KEY)
        return embeddings.embed_query(query)
