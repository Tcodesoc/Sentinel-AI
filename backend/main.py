from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.ai_explainer import explain_risk
from models import ChatRequest
from services.scanner import scan_website
from services.report import build_scan_data
from ai import generate_reply

app = FastAPI(
    title="Sentinel AI",
    description="AI-Powered Cybersecurity Assistant",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
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

    user_message = request.message.lower().strip()

    if user_message.startswith("scan"):
        url = user_message.replace("scan", "").replace(":", "").strip()

        result = scan_website(url)

        return {
            "reply": build_scan_data(result)
        }

    return {
        "reply": generate_reply(request.name, request.message)
    }