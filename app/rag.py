from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import PGVector
from app.config import settings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=settings.openai_api_key
)

COLLECTION_NAME = "runbooks"

def get_vectorstore():
    """Returns a LangChain PGVector wrapper connected to our PostgreSQL database."""
    return PGVector(
        connection_string=settings.postgres_url,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME,
        use_jsonb=True,
    )