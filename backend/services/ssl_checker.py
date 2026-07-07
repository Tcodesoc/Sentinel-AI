import ssl
import socket
from datetime import datetime


def check_ssl(url):

    try:
        hostname = (
            url.replace("https://", "")
            .replace("http://", "")
            .split("/")[0]
        )

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as ssock:

                certificate = ssock.getpeercert()
                tls_version = ssock.version()


        expiry_date = datetime.strptime(
            certificate["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        days_remaining = (
            expiry_date - datetime.utcnow()
        ).days


        issuer = dict(
            item[0] for item in certificate["issuer"]
        )


        return {
            "valid": True,
            "issuer": issuer.get(
                "organizationName",
                "Unknown"
            ),
            "expires": expiry_date.strftime(
                "%Y-%m-%d"
            ),
            "days_remaining": days_remaining,
            "tls_version": tls_version
        }


    except Exception as e:

        return {
            "valid": False,
            "issuer": None,
            "expires": None,
            "days_remaining": None,
            "tls_version": None,
            "error": str(e)
        }