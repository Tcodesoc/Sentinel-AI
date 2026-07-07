def explain_risk(result):
    score = result.get("threat_score", 0)

    if score >= 70:
        return "High risk website. Possible phishing or malicious patterns detected."
    elif score >= 30:
        return "Medium risk website. Some suspicious indicators found."
    else:
        return "Low risk website. No major threats detected."