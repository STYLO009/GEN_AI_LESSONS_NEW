from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

parser = StrOutputParser()

llm = ChatOllama(model='llama3.2')

prompt1 = PromptTemplate(
    template='Give greetings to the user on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Give him the linkedin post message on the {topic} and also use suitable professional emojis',
    input_variables=['topic']
)

chain = RunnableParallel({
    'about': prompt1 | llm | parser,
    'linkedin': prompt2 | llm | parser
})

@app.post("/generate")
def generate(request: TopicRequest):
    result = chain.invoke({'topic': request.topic})
    return result