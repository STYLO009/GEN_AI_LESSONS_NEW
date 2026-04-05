from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-R1',
    task='text-generation',
    temperature=1
)

model = ChatHuggingFace(llm = llm)

while True:
    userInput = input("I : ")
    if userInput == 'exit':
        break
    result = model.invoke(userInput)
    print("Deepseek bhai : ", result.content)