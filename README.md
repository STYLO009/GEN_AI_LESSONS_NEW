# 🤖 GenAI Project (Local LLM with Ollama)

## 📌 About

This repository contains a **Generative AI (GenAI)** application built using **Ollama** and modern LLM frameworks.
The goal of this project is to run powerful AI models **locally** for tasks like chat, reasoning, and automation.

Unlike cloud-based AI tools, this project ensures:

* 🔐 Privacy (runs completely on your machine)
* ⚡ Low latency responses
* 💻 Offline capability (after model download)

---

## 🚀 What is GenAI?

Generative AI refers to models that can **generate content** such as:

* Text 📝
* Code 💻
* Conversations 💬
* Ideas 💡

This project leverages **LLMs (Large Language Models)** to simulate intelligent responses.

---

## ✨ Features

* 🧠 Local LLM execution using Ollama
* 💬 Chat-based interaction system
* ⚡ Fast and efficient responses
* 🔄 Easy model switching (LLaMA, Mistral, etc.)
* 🛠️ Beginner-friendly setup

---

## 🛠️ Tech Stack

* Python 🐍
* Ollama 🧠
* LangChain (optional)
* Environment Variables (.env)

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/genai-project.git
cd genai-project
```

---

### 2️⃣ Setup Virtual Environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Setup Ollama

### Install Ollama

Download from: https://ollama.com

---

### Pull a Model

```bash
ollama pull llama3
```

You can also use:

```bash
ollama pull mistral
```

---

### Run the Model

```bash
ollama run llama3
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 🔄 Git Workflow (Clone → Commit → Push)

### Clone

```bash
git clone https://github.com/your-username/genai-project.git
```

### Add Changes

```bash
git add .
```

### Commit

```bash
git commit -m "Added GenAI feature"
```

### Push

```bash
git push origin main
```

---

### What about the HuggingFacemodel that can be used for sure response for Text-generation ??
The models are : 
1) meta-llama/Llama-3.1-8B-Instruct
2) deepseek-ai/DeepSeek-R1
3) qwen2.5-coder

### How to run Ollama for offline access --
- ollama pull qwen2.5-coder
- ollama run qwen2.5-coder

For sureshot access
-------

# 🤖 FastAPI AI Chat API

An AI-powered REST API built using FastAPI and Hugging Face LLM.

## 🚀 Features
- FastAPI backend
- AI Chat endpoint using Mistral-7B
- Clean modular structure
- Postman tested APIs

## 🛠️ Tech Stack
- FastAPI
- LangChain
- Hugging Face
- Python

## IF not worked 
Install the installations that are :
- pip install langchain langchain-huggingface
- pip install huggingface_hub transformers sentence-transformers

## 📂 Project Structure

```
genai-project/
│── app.py
│── requirements.txt
│── .env
│── README.md
```

---

## 💡 Use Cases

* 🤖 Chatbot development
* 🧑‍💻 Code generation
* 📚 Learning AI concepts
* 🧠 Local AI assistants

---

## 🔮 Future Scope

* 🌐 Web-based UI
* 🧾 Memory-based conversations
* 🔊 Voice interaction
* 📊 Integration with databases

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve this project.

---

## 📜 License

MIT License

---

## 🙌 Credits

* Ollama
* Open-source LLM community

---

⭐ **Star this repo if you found it helpful!**
