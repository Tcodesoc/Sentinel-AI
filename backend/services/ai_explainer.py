def explain_risk(result):

    website = result.get("website", "Unknown website")
    threat_score = result.get("threat_score", 0)
    headers = result.get("security_headers", {})

    explanation = []

    # Website status
    if result.get("status") == "Online":
        explanation.append(
            f"{website} is currently online and responding to requests."
        )
    else:
        explanation.append(
            f"{website} could not be reached during the scan."
        )

    # HTTPS analysis
    if result.get("https"):
        explanation.append(
            "HTTPS is enabled, meaning traffic is encrypted between the user and server."
        )
    else:
        explanation.append(
            "HTTPS is not enabled, which increases security risk because traffic may not be encrypted."
        )

    # Header analysis
    missing_headers = []

    if not headers.get("Strict-Transport-Security"):
        missing_headers.append("HSTS")

    if not headers.get("Content-Security-Policy"):
        missing_headers.append("CSP")

    if not headers.get("X-Frame-Options"):
        missing_headers.append("X-Frame-Options")

    if not headers.get("X-Content-Type-Options"):
        missing_headers.append("X-Content-Type-Options")


    if missing_headers:
        explanation.append(
            "Missing security protections detected: "
            + ", ".join(missing_headers)
            + "."
        )
    else:
        explanation.append(
            "All recommended security headers were detected."
        )


    # Threat analysis
    if threat_score >= 70:

        explanation.append(
            "The website shows several suspicious indicators and should be treated with caution."
        )

    elif threat_score >= 30:

        explanation.append(
            "Some suspicious indicators were found and additional investigation is recommended."
        )

    else:

        explanation.append(
            "No major threat indicators were detected during this scan."
        )


    return " ".join(explanation)