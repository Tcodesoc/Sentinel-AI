from fastapi import FastAPI

app = FastAPI(
    title="Sentinel AI",
    description="AI-Powered Cybersecurity Assistant",
    version="1.0.0"
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