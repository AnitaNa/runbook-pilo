from fastapi import  FastAPI
from pydantic import BaseModel
from app.database import init_db
from app.rag import get_vectorstore

app = FastAPI(title="RunbookPiltot API", version="1.0.0")

class DiagnoseRequest(BaseModel):
    error_message: str

# FastAPI startup event - runs automatically when the server boots up
@app.on_event("startup")
def startup_event():
    init_db

@app.get("/")
def read_route():
    return {"status": "RunbookPilot is online and ready!"}

@app.post("/diagnose")
def diagnose_error(request: DiagnoseRequest ):
    """
    Receives an error message, performs a vector similarity search against 
    our PostgreSQL pgvector runbooks, and returns the best matching resolution steps.
    """
    # Connect to vector store
    vectorstore = get_vectorstore()
    results = vectorstore.similarity_search_with_score(request.error_message, k=2)
    matches = []

    for doc, score in results:
        matches.append({
            "title": doc.metadata.get("title"),
            "service": doc.metadata.get("service"),
            "content": doc.page_content,
            "relevance_score": float(score)
        })

        return {
            "query": request.error_message,
            "matches": matches
        }