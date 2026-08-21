from service import (
    create_rag_system,
    ask_rag
)

model, retriever = create_rag_system(
   "sales_policy.txt"
) 

answer = ask_rag(
    model,
    retriever,
    "What qualifies as a high-value customer"
)

print(answer)