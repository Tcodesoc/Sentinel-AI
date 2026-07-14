def explain_risk(result):

    headers = result.get("security_headers", {})
    ssl = result.get("ssl", {})
    domain = result.get("domain", {})
    dns = result.get("dns", {})
    threat_score = result.get("threat_score", 0)

    explanations = []


    # ----------------------------
    # Security Headers
    # ----------------------------

    if not headers.get("Strict-Transport-Security"):
        explanations.append(
            "HSTS is missing, allowing browsers to fall back to insecure HTTP connections."
        )

    if not headers.get("Content-Security-Policy"):
        explanations.append(
            "Content Security Policy (CSP) is missing, increasing exposure to Cross-Site Scripting (XSS) attacks."
        )

    if not headers.get("X-Frame-Options"):
        explanations.append(
            "X-Frame-Options is missing, making the website more susceptible to clickjacking."
        )

    if not headers.get("X-Content-Type-Options"):
        explanations.append(
            "X-Content-Type-Options is missing, allowing browsers to MIME-sniff uploaded content."
        )


    # ----------------------------
    # SSL Analysis
    # ----------------------------

    if ssl:

        if ssl.get("valid"):
            explanations.append(
                f"SSL certificate is valid and uses {ssl.get('tls_version', 'a secure TLS version')}."
            )

            days = ssl.get("days_remaining")

            if days is not None and days < 30:
                explanations.append(
                    f"The SSL certificate expires in {days} days and should be renewed soon."
                )

        else:
            explanations.append(
                "No valid SSL certificate was detected."
            )


    # ----------------------------
    # Domain Analysis
    # ----------------------------

    if domain:

        age = domain.get("domain_age")

        if age is not None:

            if age >= 2:
                explanations.append(
                    f"The domain has existed for {age} years, which generally increases trust."
                )

            else:
                explanations.append(
                    "The domain is relatively new, which can increase phishing risk."
                )


    # ----------------------------
    # DNS Analysis
    # ----------------------------

    if dns:

        if dns.get("spf"):
            explanations.append(
                "SPF email protection is configured."
            )
        else:
            explanations.append(
                "SPF protection is missing."
            )

        if dns.get("dmarc"):
            explanations.append(
                "DMARC protection is enabled."
            )
        else:
            explanations.append(
                "DMARC protection is missing."
            )


    # ----------------------------
    # Threat Intelligence
    # ----------------------------

    if threat_score > 30:
        explanations.append(
            "The URL contains characteristics commonly associated with phishing or suspicious websites."
        )


    # ----------------------------
    # Overall Assessment
    # ----------------------------

    if not explanations:
        explanations.append(
            "No significant security issues were detected during the scan."
        )

    return explanations