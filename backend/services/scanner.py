import requests


def scan_website(url: str):

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5)

        headers = response.headers

        return {
            "website": url,
            "status": "Online",
            "https": url.startswith("https://"),
            "status_code": response.status_code,
            "security_headers": {
                "Strict-Transport-Security":
                    "Strict-Transport-Security" in headers,

                "Content-Security-Policy":
                    "Content-Security-Policy" in headers,

                "X-Content-Type-Options":
                    "X-Content-Type-Options" in headers,

                "X-Frame-Options":
                    "X-Frame-Options" in headers
            }
        }

    except Exception:
        return {
            "website": url,
            "status": "Offline",
            "https": False,
            "status_code": None,
            "security_headers": {
                "Strict-Transport-Security": False,
                "Content-Security-Policy": False,
                "X-Content-Type-Options": False,
                "X-Frame-Options": False
            }
        }