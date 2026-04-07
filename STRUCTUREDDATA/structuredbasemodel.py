from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

# Initialize model
llm = ChatOllama(model='qwen2.5-coder')

# Define schema using Pydantic
class Review(BaseModel):
    Key_themes: List[str] = Field(description="List all key themes discussed in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="Sentiment of the review")
    pros: Optional[List[str]] = Field(default=None, description="List of pros mentioned in the review")
    cons: Optional[List[str]] = Field(default=None, description="List of cons mentioned in the review")

# Bind structured output
structured_llm = llm.with_structured_output(Review)

# Input
review_text = """
The laptop has excellent battery life and performance is very smooth.
However, the build quality feels cheap and the keyboard is not comfortable.
Overall, a good device for students.
"""

# Invoke
result = structured_llm.invoke(review_text)

# Output
print(result)                
print(result.summary)       
print(result.sentiment)
print(result.pros)
print(result.cons)