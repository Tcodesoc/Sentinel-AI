def calculate_risk(headers, threat_score=0):

    score = 100

    # Security header penalties
    score -= 20 if not headers.get("Strict-Transport-Security") else 0
    score -= 30 if not headers.get("Content-Security-Policy") else 0
    score -= 20 if not headers.get("X-Content-Type-Options") else 0
    score -= 15 if not headers.get("X-Frame-Options") else 0

    # Threat intelligence penalty
    score -= threat_score

    # Clamp score (IMPORTANT FIX)
    score = max(0, min(score, 100))

    # Risk levels
    if score >= 80:
        risk = "🟢 Low"
    elif score >= 60:
        risk = "🟡 Medium"
    else:
        risk = "🔴 High"

    return score, risk