def calculate_risk(headers):

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

    return score, risk