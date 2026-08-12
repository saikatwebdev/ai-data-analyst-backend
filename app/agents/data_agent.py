from dotenv import load_dotenv

from langchain.agents import create_agent

from app.agents.tools import create_dataset_tools


load_dotenv()

def create_data_agent(dataset_id:str):
    tools = create_dataset_tools(dataset_id)

    return create_agent(
    model="google_genai:gemini-3.5-flash",
    tools=tools,
    system_prompt="""
    You are an AI Data Analyst.

    Your job is to answer questions about
    the user's uploaded dataset.

    Rules:

    1. Use tools for numerical calculations.
    2. Never invent numerical results.
    3. If a requested column does not exist,
        clearly explain that.
    4. If the question cannot be answered
        from the dataset, say so.
    5. Keep answers concise but explain
        the reasoning when useful.

    """
)


agent = create_data_agent()