from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

Embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=50)
result = Embedding.embed_query("Kolkata is joy")
print(str(result))