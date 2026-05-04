from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model='llama3.2'
)

while True:
    userInput = input("Me : ")
    if userInput == 'exit':
        break
    result = llm.invoke(userInput)
    print("Ollama bhai ka answer hai : ", result.content)