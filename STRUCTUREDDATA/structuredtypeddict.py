from langchain_ollama import ChatOllama
from typing import TypedDict, Optional, Annotated, Literal

# Initialize model
llm = ChatOllama(model='qwen2.5-coder')

# Define schema
class Review(TypedDict):
    Key_themes: Annotated[list[str], "List all key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg", "neutral"], "Sentiment of the review"]
    pros: Annotated[Optional[list[str]], "List of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of cons mentioned in the review"]

# Bind structured output
structured_llm = llm.with_structured_output(Review)

# Example input
review_text = """
The laptop has excellent battery life and performance is very smooth.
However, the build quality feels cheap and the keyboard is not comfortable.
Overall, a good device for students.
"""

# Invoke model
result = structured_llm.invoke(review_text)

print(result)
print(result['summary'])
print(result['sentiment'])
