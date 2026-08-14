from app.agents.data_agent import create_data_agent


dataset_id = "8881be36-ca62-43da-a917-c4ad5afed3cc"


agent = create_data_agent(dataset_id)


result = agent.invoke(
    {
        "messages":[
            {
                "role": "user",
                "content":"What is the average math score?"
            }
        ]
    }
)


print(
    result["messages"][-1].content

)