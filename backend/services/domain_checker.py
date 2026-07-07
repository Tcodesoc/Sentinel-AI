from datetime import datetime
import whois


def check_domain(domain):

    # Remove protocol if included
    domain = (
        domain
        .replace("https://", "")
        .replace("http://", "")
        .split("/")[0]
    )

    try:
        info = whois.whois(domain)

        creation = info.creation_date

        # Some WHOIS records return a list
        if isinstance(creation, list):
            creation = creation[0]

        age = None

        if creation:
            today = datetime.now()
            age = today.year - creation.year

        return {
            "domain": domain,
            "registrar": info.registrar,
            "created": str(creation),
            "domain_age": age,
            "nameservers": list(info.name_servers)
            if info.name_servers
            else []
        }

    except Exception:

        return {
            "domain": domain,
            "registrar": None,
            "created": None,
            "domain_age": None,
            "nameservers": []
        }