from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from app.graph.state import AnalystState
from app.graph.nodes import (
    run_data_agent,
    generate_final_answer,
)


def create_analyst_graph():

    graph = StateGraph(
        AnalystState
    )

    graph.add_node(
        "data_agent",
        run_data_agent
    )

    graph.add_node(
        "final_answer",
        generate_final_answer
    )

    graph.add_edge(
        START,
        "data_agent"
    )

    graph.add_edge(
        "data_agent",
        "final_answer"
    )

    graph.add_edge(
        "final_answer",
        END
    )

    return graph.compile()