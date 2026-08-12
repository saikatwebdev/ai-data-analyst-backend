from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

model = init_chat_model(
    "google_genai:gemini-3.5-flash"
)

response = model.invoke(
    "explain what a pandas dataframe is in one sentence."
)

print(response.content)