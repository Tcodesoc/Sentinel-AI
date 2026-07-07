def explain_risk(result):
    headers = result.get("security_headers", {})
    score = result.get("threat_score", 0)

    explanations = []

    if not headers.get("Strict-Transport-Security"):
        explanations.append(
            "This website does not enforce HTTPS strictly. Attackers could downgrade connections."
        )

    if not headers.get("Content-Security-Policy"):
        explanations.append(
            "Missing CSP increases risk of XSS (Cross-Site Scripting) attacks."
        )

    if not headers.get("X-Frame-Options"):
        explanations.append(
            "Site is vulnerable to clickjacking attacks due to missing frame protection."
        )

    if score > 30:
        explanations.append(
            "URL contains suspicious patterns that slightly increase phishing risk."
        )

    if not explanations:
        explanations.append(
            "No major security issues detected. The site follows good basic security practices."
        )

    return explanations