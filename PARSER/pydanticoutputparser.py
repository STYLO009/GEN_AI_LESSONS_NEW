from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatOllama(
    model='qwen2.5-coder'
)

class Person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(gt=18, description='Age of the person')
    city : str = Field(description='City of the person')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate a brief description of the person and the person belongs to which {place} \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)

prompt = template.invoke({'place' : 'indian'})
result = llm.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)