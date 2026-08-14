from app.graph.analyst_graph import (
    create_analyst_graph
)


graph = create_analyst_graph()


result = graph.invoke(
    {
        'dataset_id': "d1541246-ada0-450b-a130-77407486428c",
        "user_question":"What is the average math score?",
        "analysis_result":"",
        "final_answer":"",
    }
)


print(result)