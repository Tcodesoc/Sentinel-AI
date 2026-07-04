from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="Sentinel AI",
    description="AI-Powered Cybersecurity Assistant",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    name: str
    message: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Sentinel AI 🚀",
        "status": "Online"
    }


@app.get("/health")
def health():
    return {
        "server": "Healthy",
        "database": "Coming Soon",
        "ai": "Coming Soon"
    }


@app.get("/about")
def about(name: str):
    return {
        "application": "Sentinel AI",
        "developer": name,
        "version": "1.0"
    }


@app.get("/hello")
def hello(name: str):
    return {
        "message": f"Hello {name}, welcome to Sentinel AI!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message.lower()

    if "hello" in user_message:
        reply = f"Hello {request.name}! Nice to meet you."

    elif "scan" in user_message:
        reply = "Website scanning is coming soon."

    elif "help" in user_message:
        reply = "I can help with cybersecurity questions."

    else:
        reply = "I'm still learning. Ask me something else."

    return {
        "reply": reply
    }