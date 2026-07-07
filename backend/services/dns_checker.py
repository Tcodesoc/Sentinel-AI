import dns.resolver


def check_dns(domain):

    # Remove protocol if included
    domain = (
        domain
        .replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
    )

    result = {
        "domain": domain,
        "a_records": [],
        "mx_records": [],
        "txt_records": [],
        "ns_records": [],
        "spf": False,
        "dmarc": False
    }


    # A Records
    try:
        answers = dns.resolver.resolve(domain, "A")

        for ip in answers:
            result["a_records"].append(str(ip))

    except Exception:
        pass


    # MX Records
    try:
        answers = dns.resolver.resolve(domain, "MX")

        for mail in answers:
            result["mx_records"].append(str(mail.exchange))

    except Exception:
        pass


    # TXT Records
    try:
        answers = dns.resolver.resolve(domain, "TXT")

        for txt in answers:
            value = str(txt)

            result["txt_records"].append(value)

            if "v=spf1" in value.lower():
                result["spf"] = True

    except Exception:
        pass


    # DMARC
    try:
        answers = dns.resolver.resolve(
            "_dmarc." + domain,
            "TXT"
        )

        for txt in answers:
            if "v=dmarc" in str(txt).lower():
                result["dmarc"] = True

    except Exception:
        pass


    # Nameservers
    try:
        answers = dns.resolver.resolve(domain, "NS")

        for ns in answers:
            result["ns_records"].append(str(ns))

    except Exception:
        pass


    return result