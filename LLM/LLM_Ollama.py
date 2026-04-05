from ollama import chat

response = chat(
    model='qwen2.5-coder',
    messages=[{'role': 'user', 'content': 'India is great ??'}],
)
print(response.message.content)