from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
Documents = [
    "Kolkata is Joy",
    "My name is Hella",
    "How are you??"
]
result = embedding.embed_documents(Documents)

print(str(result))