from fastapi import FastAPI
from model import User
from llm import llm

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Server running 🚀"}

@app.post("/create-user")
def create_user(user: User):
    return {"user": user}

@app.get("/chat")
def chat(q: str):
    response = llm.invoke(q)
    return {"response": str(response)}