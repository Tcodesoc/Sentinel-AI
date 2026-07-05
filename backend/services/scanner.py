import requests


def scan_website(url: str):

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5)

        return {
            "website": url,
            "status": "Online",
            "https": url.startswith("https://"),
            "status_code": response.status_code
        }

    except Exception:
        return {
            "website": url,
            "status": "Offline",
            "https": False,
            "status_code": None
        }