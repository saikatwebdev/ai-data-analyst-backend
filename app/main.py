from fastapi import FastAPI
from app.api.datasets import router as datasets_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router






app = FastAPI(
    title="AI Data Analyst API",
    description="Backend API for the AI Data Analyst and Business INtelligence Agent",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],

)

app.include_router(datasets_router)
app.include_router(chat_router)




@app.get("/")
def home():
    return {
        "message": "AI Data Analyst API is Running"
    }






