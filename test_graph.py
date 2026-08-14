from app.graph.analyst_graph import create_analyst_graph


graph = create_analyst_graph()

print(
    graph.get_graph().draw_ascii()
)