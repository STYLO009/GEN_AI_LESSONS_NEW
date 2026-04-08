from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import Optional, Annotated, TypedDict
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(
    model="qwen2.5-coder"
)

template1 = PromptTemplate(
    template="Write a detailed inofrmation about {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="write a brief understanding about {topic}",
    input_variables=['topic']
)

prompt1 = template1.invoke({'topic' : 'Sun rises in the East??'})
result1 = llm.invoke(prompt1)

prompt2 = template2.invoke({'topic' : 'Sun rises in the East??'})
result2 = llm.invoke(prompt1)

print(result1.content)

print("-"*60)

print(result2.content)