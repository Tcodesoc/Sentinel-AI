def calculate_risk(headers, threat_score=0, ssl=None, domain=None, dns=None):

    score = 100


    # ----------------------------
    # SECURITY HEADER PENALTIES
    # ----------------------------

    score -= 20 if not headers.get("Strict-Transport-Security") else 0

    score -= 30 if not headers.get("Content-Security-Policy") else 0

    score -= 20 if not headers.get("X-Content-Type-Options") else 0

    score -= 15 if not headers.get("X-Frame-Options") else 0



    # ----------------------------
    # THREAT INTELLIGENCE
    # ----------------------------

    score -= threat_score



    # ----------------------------
    # SSL INTELLIGENCE
    # ----------------------------

    if ssl:

        if not ssl.get("valid"):
            score -= 40

        days = ssl.get("days_remaining")

        if days is not None:

            if days < 30:
                score -= 15



    # ----------------------------
    # DOMAIN INTELLIGENCE
    # ----------------------------

    if domain:

        age = domain.get("domain_age")

        # domain_age is returned in YEARS
        if age is not None:

            if age < 1:
                score -= 30

            elif age < 2:
                score -= 15



    # ----------------------------
    # DNS INTELLIGENCE
    # ----------------------------

    if dns:

        if not dns.get("spf"):
            score -= 10

        if not dns.get("dmarc"):
            score -= 10



    # ----------------------------
    # SCORE LIMIT
    # ----------------------------

    score = max(0, min(score, 100))



    # ----------------------------
    # RISK LEVEL
    # ----------------------------

    if score >= 80:
        risk = "🟢 Low"

    elif score >= 60:
        risk = "🟡 Medium"

    else:
        risk = "🔴 High"


    


    return score, risk