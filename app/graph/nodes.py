from app.agents.data_agent import create_data_agent
from app.graph.state import AnalystState


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