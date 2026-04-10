from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from typing import Literal
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field

llm = ChatOllama(
    model='llama3.2'
)

class Feedback(BaseModel):
    sentiment : Literal['Positive', 'Negative', 'Neutral'] = Field(description='Give the sentiment Analysis of the user.')

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template="Check the sentiment analysis of the user when he is giving {feedback} \n \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classify_chain = prompt | llm | parser
result = classify_chain.invoke({
    'feedback' : 'I am feeling very Happy ;)'
})

print(result)

classify_chain.get_graph().print_ascii()