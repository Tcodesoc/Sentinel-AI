from services.risk import calculate_risk


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

    score, risk = calculate_risk(headers)

    return {
        "website": result["website"],
        "status": result["status"],
        "https": result["https"],
        "status_code": result["status_code"],
        "headers": headers,
        "score": score,
        "risk": risk,
        "recommendations": recommendations
    }


def build_report(result):

    data = build_scan_data(result)

    headers = data["headers"]

    return f"""
🛡️ Sentinel AI Security Report

Website: {data['website']}

Status: {data['status']}
HTTPS: {data['https']}
HTTP Code: {data['status_code']}

Security Headers
----------------
Strict-Transport-Security: {'✅' if headers['Strict-Transport-Security'] else '❌'}
Content-Security-Policy: {'✅' if headers['Content-Security-Policy'] else '❌'}
X-Content-Type-Options: {'✅' if headers['X-Content-Type-Options'] else '❌'}
X-Frame-Options: {'✅' if headers['X-Frame-Options'] else '❌'}

Risk Score: {data['score']}/100
Overall Risk: {data['risk']}

Recommendations
---------------
{chr(10).join(data['recommendations'])}
"""