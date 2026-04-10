from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = ChatOllama(
    model="qwen2.5-coder"
)

schema = [
    ResponseSchema(name='fact_1', description='fact1 about the topic'),
    ResponseSchema(name='fact_2', description='fact2 about the topic'),
    ResponseSchema(name='fact_3', description='fact3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

format_instructions = parser.get_format_instructions()

template = PromptTemplate(
    template='Give facts on the topic: {topic}\n{format_instructions}',
    input_variables=['topic'],
    partial_variables={"format_instructions": format_instructions}
)

# Create final prompt
query = template.format(topic="Artificial Intelligence")

# Call LLM
response = llm.invoke(query)

# Parse output
parsed_output = parser.parse(response.content)

print(parsed_output)