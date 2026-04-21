from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

loader = TextLoader('D:\GEN_AI\RAG\india.txt', encoding='utf-8')
docs = loader.load()

llm = ChatOllama(
    model='llama3.2'
)

prompt = PromptTemplate(
    template='Write a brief summary on the {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke(
    {'topic' : docs[0].page_content}
)

print(result)