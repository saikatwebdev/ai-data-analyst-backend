from app.agents.data_agent import create_data_agent
from app.graph.state import AnalystState


def classify_question(
        state:AnalystState
)-> AnalystState:
    question = state["user_question"].lower()
    data_keywords = [
        "revenue",
        "profit",
        "rows",
        "columns",
        "average",
        "median",
        "maximum",
        "minimum",
        "mean",
        "correlation",
        "outlier",
        "missing",
        "duplicate",
        "dataset",
        "product",
        "region"
    ]


    is_data_question = any(
        keyword in question
        for keyword in data_keywords
    )

    intent = (
        "data"
        if is_data_question
        else "general"
    )

    print("\n==============================")
    print("QUESTION:", question)
    print("INTENT:", intent)
    print("==============================\n")

    return {
        **state,
        "intent": intent,
    }



def run_data_agent(
    state: AnalystState
) -> AnalystState:

    dataset_id = state["dataset_id"]

    question = state["user_question"]

    agent = create_data_agent(
        dataset_id
    )

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    answer = result["messages"][-1].content

    return {
        **state,
        "analysis_result": answer,
    }


def generate_final_answer(
    state: AnalystState
) -> AnalystState:

    return {
        **state,
        "final_answer": state["analysis_result"],
    }



def general_response(state:AnalystState)->AnalystState:
    return {
        **state,
        "final_answer":(
            "I am designed primarily to analyze "
            "your uploaded datasets. Please ask me "
            "a question related to the dataset."
        ),
    }

def route_question(state:AnalystState)->str:
    return state["intent"]