from datetime import datetime
from services.risk import calculate_risk
from services.ai_explainer import explain_risk


def build_scan_data(result):

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

    score, risk = calculate_risk(
        headers,
        result.get("threat_score", 0),
        result.get("ssl"),
        result.get("domain"),
        result.get("dns")
    )

    passed = sum(
        1 for v in headers.values() if v
    )

    total = len(headers)

    return {
        "website": result["website"],
        "status": result["status"],
        "https": result["https"],
        "status_code": result["status_code"],
        "response_time": result.get("response_time"),

        "headers": headers,

        "score": score,
        "risk": risk,

        "recommendations": recommendations,

        "scan_time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "passed_headers": passed,
        "total_headers": total,

        "explanations": explain_risk(result),

        "ssl": result.get("ssl"),

        "domain": result.get("domain"),

        "dns": result.get("dns"),

        "ports": result.get("ports")
    }