from langchain_community.vectorstores import FAISS

from embeddings import get_embeddings


def create_vector_store(
        documents
):
    embeddings = get_embeddings()

    return FAISS.from_documents(
        documents,
        embeddings,
    )