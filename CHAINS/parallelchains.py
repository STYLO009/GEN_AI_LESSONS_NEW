from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm1 = ChatOllama(model='qwen2.5-coder')
llm2 = ChatOllama(model='llama3.2')

prompt1 = PromptTemplate(
    template='Give some of the questions on {quiz}',
    input_variables=['quiz']
)

prompt2 = PromptTemplate(
    template='Give answers of the questions: {quiz}',
    input_variables=['quiz']
)

prompt3 = PromptTemplate(
    template='Make a conclusion using these notes:\n{notes}\n\nand answers:\n{text}',
    input_variables=['notes', 'text']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | llm1 | parser,
    'text': prompt2 | llm2 | parser
})

merge_chain = prompt3 | llm2 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({
    "quiz": "Artificial Intelligence"
})

print(result)
chain.get_graph().print_ascii()