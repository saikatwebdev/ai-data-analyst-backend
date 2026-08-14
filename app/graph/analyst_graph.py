from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from app.graph.state import AnalystState
from app.graph.nodes import (
    classify_question,
    route_question,
    run_data_agent,
    general_response,
    generate_final_answer,

)


def create_analyst_graph():

    graph = StateGraph(
        AnalystState
    )

    graph.add_node(
        "classifier",
        classify_question
    )

    graph.add_node(
        "data_agent",
        run_data_agent
    )
    graph.add_node(
        "general",
        general_response
    )
    graph.add_node(
        "final_answer",
        generate_final_answer
    )

    # Start to classifier
    # here classifier will part the intent as general and data.
    graph.add_edge(
        START,
        "classifier"
    )

    graph.add_conditional_edges(
        "classifier",
        route_question,
        {
            "data": "data_agent",
            "general": "general"
        }
    )

    graph.add_edge(
        "data_agent",
        "final_answer"
    )

    graph.add_edge(
        "general",
        END
    )
    graph.add_edge(
        "final_answer",
        END
    )

    return graph.compile()