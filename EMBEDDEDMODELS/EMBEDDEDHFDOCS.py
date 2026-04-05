from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

Documents = [
    "India is great",
    "Pakistan is the son of India",
    "India is the father of pakistan",
    "India is the Independent country",
    "India contains 3 billion people all across"
]

query = 'Who is the father of Pakistan'

doc_embeddings = embeddings.embed_documents(Documents)
query_embeddings = embeddings.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]
index, scores = sorted(list(enumerate(scores)), key = lambda x : x[1])[-1]

print(query)
print(Documents[index])
print(scores)