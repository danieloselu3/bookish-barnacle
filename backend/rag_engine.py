from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
import os

VECTOR_DIR = os.path.join(os.getcwd(), "vectorstore")

def retrieve_context(query: str):
    """Retrieves context from Chroma vector DB for a given query."""
    db = Chroma(
        persist_directory=VECTOR_DIR,
        embedding_function=OllamaEmbeddings(model="llama3")
    )
    retriever = db.as_retriever()
    docs = retriever.get_relevant_documents(query)
    return "\n".join([d.page_content for d in docs]) if docs else "No context found."
