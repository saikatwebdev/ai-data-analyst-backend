from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)



def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=20,
        chunk_overlap=5
    )

    return splitter.split_documents(
        documents
    )
   
