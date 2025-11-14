<<<<<<< HEAD
# 🤖 RAG Chatbot with LangGraph & Ollama

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange.svg)
![Ollama](https://img.shields.io/badge/Ollama-llama3.2-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A powerful **Retrieval-Augmented Generation (RAG)** chatbot built with **LangGraph** and **Ollama**. 

Ask questions about Large Language Models and get accurate, context-aware answers powered by Wikipedia knowledge base.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Demo](#-demo)

</div>

---

## ✨ Features

- 🧠 **Intelligent RAG System** - Combines retrieval and generation for accurate answers
- 🔄 **LangGraph Workflow** - Modular, maintainable agent architecture
- 🏠 **Local LLM** - Runs completely offline using Ollama (llama3.2)
- 📚 **Vector Database** - FAISS-powered semantic search
- ⚡ **Fast Embeddings** - Nomic embed-text for quick document retrieval
- 💬 **Interactive CLI** - User-friendly command-line interface
- 🔧 **Fully Configurable** - Easy customization via environment variables
- 📦 **Modular Design** - Clean separation of concerns

## 🏗️ Architecture

```mermaid
graph LR
    A[User Question] --> B[Retrieve Documents]
    B --> C[Vector Store FAISS]
    C --> D[Top-K Documents]
    D --> E[Generate Response]
    E --> F[LLM llama3.2]
    F --> G[Final Answer]
```

### Project Structure

=======
# -RAG-Chatbot-with-LangGraph
>>>>>>> 8124430b5ee275e6a7574c4edfd4db9bc781fcfe
