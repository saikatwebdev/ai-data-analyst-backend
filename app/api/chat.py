from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.graph.analyst_graph import create_analyst_graph
from app.services.dataset_store import get_dataset


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    dataset_id: str
    message: str


@router.post("/")
async def chat(request: ChatRequest):

    df = get_dataset(request.dataset_id)

    if df is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found."
        )

    graph = create_analyst_graph()

    result = graph.invoke(
        {
            "dataset_id": request.dataset_id,

            "user_question": request.message,

            "analysis_result": "",

            "business_context": "",

            "insights": "",

            "final_answer": "",
        }
    )

    return {
        "dataset_id": request.dataset_id,

        "question": request.message,

        "answer": result["final_answer"],
    }