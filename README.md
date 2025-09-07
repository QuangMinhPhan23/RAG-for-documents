# RAG for Documents

A simple, production-ready Retrieval-Augmented Generation (RAG) pipeline for document search and question answering. This project uses ChromaDB for vector storage, Sentence Transformers for semantic embeddings, and OpenAI GPT for concise answer generation. It features a Streamlit front end for interactive querying, allowing users to ask questions and receive summarized, context-aware answers from their document collection.

## Features
- Ingests and chunks text documents for semantic search
- Stores embeddings and metadata in ChromaDB
- Retrieves relevant document chunks using semantic similarity
- Summarizes answers with OpenAI GPT for clarity and brevity
- User-friendly Streamlit interface for real-time Q&A

## Use Cases
- Internal knowledge base search
- Document Q&A for teams and organizations
- Semantic search for technical, legal, or research documents

## Tech Stack
- Python
- ChromaDB
- Sentence Transformers
- OpenAI GPT
- Streamlit

### Prerequisites

- [OpenAI API Key](https://platform.openai.com/account/api-keys)

### Usage
1. Place your `.txt` documents in the `document/` folder.
2. Run the ingestion and RAG pipeline:
    ```bash
    python RAG/rag.py
    ```
3. Start the Streamlit app:
    ```bash
    streamlit run RAG/streamlit_app.py
    ```
4. Enter your OpenAI API key when prompted or set it as an environment variable:
    ```bash
    export OPENAI_API_KEY=your-key-here

# RAG for Documents

A simple, production-ready Retrieval-Augmented Generation (RAG) pipeline for document search and question answering. This project uses ChromaDB for vector storage, Sentence Transformers for semantic embeddings, and OpenAI GPT for concise answer generation. It features a Streamlit front end for interactive querying, allowing users to ask questions and receive summarized, context-aware answers from their document collection.

## Features
- Ingests and chunks text documents for semantic search
- Stores embeddings and metadata in ChromaDB
- Retrieves relevant document chunks using semantic similarity
- Summarizes answers with OpenAI GPT for clarity and brevity
- User-friendly Streamlit interface for real-time Q&A

## Use Cases
- Internal knowledge base search
- Document Q&A for teams and organizations
- Semantic search for technical, legal, or research documents

## Tech Stack
- Python
- ChromaDB
- Sentence Transformers
- OpenAI GPT
- Streamlit

### Prerequisites

- [OpenAI API Key](https://platform.openai.com/account/api-keys)

### Usage
1. Place your `.txt` documents in the `document/` folder.
2. Run the ingestion and RAG pipeline:
    ```bash
    python RAG/rag.py
    ```
3. Start the Streamlit app:
    ```bash
    streamlit run RAG/streamlit_app.py
    ```
4. Enter your OpenAI API key when prompted or set it as an environment variable:
    ```bash
    export OPENAI_API_KEY=your-key-here
The app will retrieve relevant document chunks and summarize the answer for you.
<img width="863" height="818" alt="Screenshot 2025-09-07 122021" src="https://github.com/user-attachments/assets/c21aeb10-4b5f-4da0-a61b-707429deb23c" />


