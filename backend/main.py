from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ChatRequest
from services.scanner import scan_website
from ai import generate_reply
app = FastAPI(
    title="Sentinel AI",
    description="AI-Powered Cybersecurity Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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

    if "scan" in user_message:
        url = user_message.replace("scan", "").strip()
        result = scan_website(url)

        reply = (
            f"Website: {result['website']}\n"
            f"Status: {result['status']}\n"
            f"HTTPS: {result['https']}\n"
            f"HTTP Code: {result['status_code']}"
        )

    else:
        reply = generate_reply(
            request.name,
            request.message
        )

    return {
        "reply": reply
    }

