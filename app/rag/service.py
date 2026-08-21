from langchain.chat_models import init_chat_model

from loader import load_text_file
from splitter import split_documents
from vector_store import create_vector_store
from retriever import create_retriever

def create_rag_system(
        file_path:str
):
    documents = load_text_file(file_path)

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    retriever = create_retriever(vector_store)

    model = init_chat_model(
        "google_genai:gemini-3.5-flash"
    )

    return model, retriever


def ask_rag(model, retriever, question:str):

    documents = retriever.invoke(question)
    
    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt =  f"""
You are a business knowledge assistant.
Answer the user's using only the provided context.
If the answer is not present in the context,
say that the information is not available.
Do not invent facts.

Context: 
{context}
Question:
{question}
"""
    response = model.invoke(prompt)

    return [response.content ,retriever]
