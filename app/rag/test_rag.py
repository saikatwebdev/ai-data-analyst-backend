from loader import load_text_file
from splitter import split_documents



documents = load_text_file(
    "sales_policy.txt"
)


chunks = split_documents(
    documents
)

print(
    "Documents:",
    len(documents)
)

print("Chunks:",
      len(chunks)
)

for i, chunk in enumerate(chunks):

    print(
        f"\n--- Chunk {i+1} ---"
    )

    print(
        chunk.page_content
    )

