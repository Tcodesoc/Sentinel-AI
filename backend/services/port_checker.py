import socket
from urllib.parse import urlparse

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Alt"
}


def check_ports(url: str):

    if url.startswith("http://") or url.startswith("https://"):
        host = urlparse(url).hostname
    else:
        host = url

    results = []

    for port, service in COMMON_PORTS.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        try:
            status = sock.connect_ex((host, port))
            is_open = (status == 0)
        except Exception:
            is_open = False

        results.append({
            "port": port,
            "service": service,
            "open": is_open
        })

        sock.close()

    return {
        "host": host,
        "ports": results
    }