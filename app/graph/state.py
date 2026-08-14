from typing import TypedDict


class AnalystState(TypedDict):

    dataset_id: str

    user_question: str

    intent:str

    analysis_result: str

    business_context: str

    insights: str

    final_answer: str
