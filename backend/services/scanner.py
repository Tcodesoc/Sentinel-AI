import time
import requests
import re
from services.ssl_checker import check_ssl


def scan_website(url: str):

    # Normalize URL
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        start = time.time()

        response = requests.get(
            url,
            timeout=5
        )

        elapsed = round(
            (time.time() - start) * 1000
        )

        headers = response.headers


        # ----------------------------
        # SECURITY HEADERS CHECK
        # ----------------------------
        security_headers = {
            "Strict-Transport-Security":
                "Strict-Transport-Security" in headers,

            "Content-Security-Policy":
                "Content-Security-Policy" in headers,

            "X-Content-Type-Options":
                "X-Content-Type-Options" in headers,

            "X-Frame-Options":
                "X-Frame-Options" in headers
        }


        # ----------------------------
        # BASIC THREAT INTELLIGENCE
        # ----------------------------
        suspicious_keywords = [
            "login",
            "verify",
            "bank",
            "secure",
            "account",
            "update",
            "password"
        ]

        threat_score = 0

        url_lower = url.lower()

        for word in suspicious_keywords:
            if word in url_lower:
                threat_score += 5


        # HTTP increases risk
        if url.startswith("http://"):
            threat_score += 20


        # Long numbers can indicate suspicious URLs
        if re.search(r"\d{4,}", url):
            threat_score += 10


        # ----------------------------
        # SSL CHECK
        # ----------------------------
        ssl_data = check_ssl(url)


        return {
            "website": url,
            "status": "Online",
            "https": url.startswith("https://"),
            "status_code": response.status_code,
            "response_time": elapsed,
            "threat_score": threat_score,
            "security_headers": security_headers,
            "ssl": ssl_data
        }


    except Exception:

        return {
            "website": url,
            "status": "Offline",
            "https": False,
            "status_code": None,
            "response_time": None,
            "threat_score": 100,

            "security_headers": {
                "Strict-Transport-HSTS": False,
                "Content-Security-Policy": False,
                "X-Content-Type-Options": False,
                "X-Frame-Options": False
            },

            "ssl": {
                "valid": False,
                "issuer": None,
                "expires": None,
                "days_remaining": None,
                "tls_version": None
            }
        }