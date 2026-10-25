from sqlalchemy import create_engine, text
from app.config import settings

# Created a database engine using connection string
engine = create_engine(settings.postgres_url)

def init_db():
    """Initializes the database by enabling pgvector and creating the runbook table."""
    with engine.connect() as connection:
        # Enable the pgvector extension in PostgreSQL
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))

        # Create the runbooks table if it doesn't already exist
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS runbooks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                embedding VECTOR(1536)
            );
        """))
        connection.commit()

    print("Database tables and pgvector extension initialized successfully!")