from langchain_ollama import ChatOllama
from typing import TypedDict

# Load model properly
llm = ChatOllama(model="qwen2.5-coder")

# Schema
class Review(TypedDict):
    summary: str
    sentiment: str

# Structured output
SM = llm.with_structured_output(Review)

prompt = """
Analyze the following text and return:
1. summary
2. sentiment (positive, negative, neutral)

Text:
Hey I want to talk with your manager as he ditched me in the middle of our friendship
"""

result = SM.invoke(prompt)

print(result)
print(result["summary"])
print(result["sentiment"])