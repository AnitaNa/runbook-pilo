from langchain_core.documents import Document
from app.rag import get_vectorstore

sample_runbooks = [
    Document(
        page_content="Error: Database Connection Timeout (Error 504). Cause: Connection pool exhausted in PostgreSQL or max connections reached. Resolution: 1. Check active database connections using SELECT * FROM pg_stat_activity;. 2. Restart the FastAPI application to clear stuck threads. 3. Adjust max_connections in postgresql.conf if traffic is high.",
        metadata={"title": "Database Connection Timeout 504", "service": "database"}
    ),
    Document(
        page_content="Error: Out of Memory (OOM) Killed in Docker Container. Cause: Container exceeded its RAM limit (e.g., 512MB) during large vector embedding generation or heavy API requests. Resolution: 1. Inspect container exit code using docker inspect. 2. Increase memory limit in your Docker configuration or Google Cloud Run service settings. 3. Optimize batch sizes for text chunking.",
        metadata={"title": "Docker OOM Killed Error", "service": "devops"}
    )
]

def seed_database():
    """Takes sample runbook documents, generates embeddings via OpenAI, and stores them in pgvector."""
    print("Initializing vector store connection...")
    vectorstore = get_vectorstore()
    print("Embedding and seeding sample runbooks into PostgreSQL...")
    
    vectorstore.add_documents(sample_runbooks)
    print("Sample runbooks successfully seeded and indexed!")

if __name__ == "__main__":
    seed_database()