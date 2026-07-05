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
        print(result)

        headers = result["security_headers"]

        recommendations = []

        if not headers["Strict-Transport-Security"]:
            recommendations.append(
                "Enable Strict-Transport-Security to enforce HTTPS."
            )

        if not headers["Content-Security-Policy"]:
            recommendations.append(
                "Add a Content-Security-Policy header to reduce XSS risk."
            )

        if not headers["X-Content-Type-Options"]:
            recommendations.append(
                "Enable X-Content-Type-Options to prevent MIME sniffing."
            )

        if not headers["X-Frame-Options"]:
            recommendations.append(
                "Enable X-Frame-Options to help prevent clickjacking."
            )

        if len(recommendations) == 0:
            recommendations.append(
                "Excellent! No missing security headers were detected."
            )

        score = 100

        if not headers["Strict-Transport-Security"]:
            score -= 20

        if not headers["Content-Security-Policy"]:
            score -= 30

        if not headers["X-Content-Type-Options"]:
            score -= 20

        if not headers["X-Frame-Options"]:
            score -= 15

        if score >= 80:
            risk = "🟢 Low"
        elif score >= 60:
            risk = "🟡 Medium"
        else:
            risk = "🔴 High"

        reply = f"""
🛡️ Sentinel AI Security Report

Website: {result['website']}

Status: {result['status']}
HTTPS: {result['https']}
HTTP Code: {result['status_code']}

Security Headers
----------------
Strict-Transport-Security: {'✅' if headers['Strict-Transport-Security'] else '❌'}
Content-Security-Policy: {'✅' if headers['Content-Security-Policy'] else '❌'}
X-Content-Type-Options: {'✅' if headers['X-Content-Type-Options'] else '❌'}
X-Frame-Options: {'✅' if headers['X-Frame-Options'] else '❌'}

Risk Score: {score}/100
Overall Risk: {risk}

Recommendations
---------------
{chr(10).join(recommendations)}
"""

    else:

        reply = generate_reply(
            request.name,
            request.message
        )

    return {
        "reply": reply
    }