import os
import pinecone
from .embedding_manager import PineconeEmbeddingManager
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
import logging
from dotenv import load_dotenv, find_dotenv
# Load environment variables
load_dotenv(find_dotenv())

API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")
NAMESPACE = os.getenv("NAMESPACE")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
OPENAI_API_KEY=os.getenv("API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Pinecone Manager
pinecone.init(api_key=API_KEY, environment="us-west1-gcp")
index = pinecone.Index(INDEX_NAME)

def load_documents(directory: str) -> list:
    """
    Loads text documents from a specified directory.
    """
    try:
        logging.info(f" Loading documents from {directory}...")
        loader = DirectoryLoader(directory, glob="**/*.txt")  # Modify for PDFs, CSVs, etc.
        docs = loader.load()
        logging.info(f"Loaded {len(docs)} documents.")
        return docs
    except Exception as e:
        logging.error(f"Error extracting document {directory}: {e}")
        return ""

def process_and_store_documents(directory: str):
    """
    Processes documents: splits, embeds, and stores them in Pinecone.
    """
    documents = load_documents(directory)

    if not documents:
        print("[WARNING] No documents found.")
        return

    # Initialize embedding model
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL, openai_api_key=OPENAI_API_KEY)

    # Split documents into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    all_texts = [doc.page_content for doc in documents]
    chunks = splitter.split_text("\n".join(all_texts))

    logging.info(f"Split documents into {len(chunks)} chunks.")

    # Generate embeddings
    logging.info("Generating embeddings...")
    embeddings = embedding_model.embed_documents(chunks)

    # Store embeddings in Pinecone
    logging.info("Storing embeddings in Pinecone...")
    vectors = [
        {"id": str(i), "values": embedding, "metadata": {"text": chunk}}
        for i, (embedding, chunk) in enumerate(zip(embeddings, chunks))
    ]
    
    index.upsert(vectors)
    logging.info("[SUCCESS] Documents successfully stored in Pinecone!")

if __name__ == "__main__":
    process_and_store_documents("data/documents")  # Modify directory as needed
