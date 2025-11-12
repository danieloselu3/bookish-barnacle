# Bookish Barnacle

Bookish Barnacle is a multi-service application for context-aware document retrieval and analysis using LLMs and vector databases. It leverages FastAPI, Ollama, ChromaDB, and Streamlit for a complete backend and frontend experience.

## Features

- **LLM-powered context retrieval** using Ollama models (e.g., Llama 3)
- **Vector database** for efficient document search (ChromaDB)
- **REST API** backend (FastAPI)
- **Streamlit UI** for user interaction
- **Dockerized** for easy deployment

## Project Structure

```
bookish-barnacle/
├── backend/         # FastAPI backend source code
├── ui/              # Streamlit frontend source code
├── data/            # Data files (e.g., individuals.json)
├── vectorstore/     # Persistent vector database storage
├── docker-compose.yml
└── README.md
```

## Prerequisites

- [Docker](https://www.docker.com/)
- [Ollama](https://ollama.com/) (if running locally, or use the provided Docker service)

## Setup & Usage

1. **Pull the required Ollama model (e.g., llama3):**
   ```sh
   docker-compose up -d llm
   docker exec -it llm ollama pull llama3
   ```

2. **Start all services:**
   ```sh
   docker-compose up -d
   ```

3. **Access the UI:**
   - Open [http://localhost:8501](http://localhost:8501) in your browser.

4. **API Endpoints:**
   - Backend API available at [http://localhost:5000](http://localhost:5000)

## Environment Variables

- `OLLAMA_HOST`: URL for Ollama server (default: `http://llm:11434`)
- `CHROMA_URL`: URL for ChromaDB server (default: `http://vectorstore:8000`)
- `BACKEND_URL`: URL for backend API (used by UI)

## Data

- Example data file: `data/individuals.json`

## Troubleshooting

- **Model not found:**  
  Make sure you have pulled the required model in the Ollama container.
- **Connection errors:**  
  Ensure all services are running and accessible via Docker Compose.

## License

MIT License
