from fastapi import FastAPI
from app.api.datasets import router as datasets_router






app = FastAPI(
    title="AI Data Analyst API",
    description="Backend API for the AI Data Analyst and Business INtelligence Agent",
    version="0.1.0",
)

app.include_router(datasets_router)


@app.get("/")
def home():
    return {
        "message": "AI Data Analyst API is Running"
    }






