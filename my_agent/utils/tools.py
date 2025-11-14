"""
Tools and utilities for the RAG application.
Handles initialization of LLM, embeddings, and vector database.
"""

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_llm():
    """Initialize and return the LLM."""
    print("🔧 Initializing Ollama LLM...")
    try:
        llm = ChatOllama(model="llama3.2", temperature=0.7)
        print("✓ LLM initialized successfully\n")
        return llm
    except Exception as e:
        print(f"❌ Error initializing Ollama LLM: {e}")
        print("Make sure Ollama is running with: ollama serve")
        print("And pull the model with: ollama pull llama3.2\n")
        raise


def get_embeddings():
    """Initialize and return embeddings model."""
    print("🔧 Initializing embeddings model...")
    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        print("✓ Embeddings initialized successfully\n")
        return embeddings
    except Exception as e:
        print(f"❌ Error initializing embeddings: {e}")
        print("Make sure to pull the model with: ollama pull nomic-embed-text\n")
        raise


def get_retriever():
    """Load documents and create vector store retriever."""
    print("📚 Loading documents from Wikipedia...")
    try:
        loader = WebBaseLoader("https://en.wikipedia.org/wiki/Large_language_model")
        docs = loader.load()
        print(f"✓ Loaded {len(docs)} documents")
    except Exception as e:
        print(f"❌ Error loading documents: {e}\n")
        raise

    print("✂️ Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(docs)
    print(f"✓ Created {len(splits)} chunks")

    print("🔍 Creating vector store with embeddings...")
    print("   This may take a moment as it processes embeddings...")
    try:
        embeddings = get_embeddings()
        vectorstore = FAISS.from_documents(
            documents=splits,
            embedding=embeddings
        )
        retriever = vectorstore.as_retriever()
        print("✓ Vector store created\n")
        return retriever
    except Exception as e:
        print(f"❌ Error creating vector store: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure Ollama is running: ollama serve")
        print("2. Make sure the embedding model is pulled: ollama pull nomic-embed-text")
        print("3. Try restarting Ollama and the application\n")
        raise
