from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import Optional, Annotated, TypedDict
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="qwen2.5-coder"
)

template1 = PromptTemplate(
    template="Write a detailed inforrmation about {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="write a brief understanding about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()
chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({"topic" : "Hanuman"})
print(result)