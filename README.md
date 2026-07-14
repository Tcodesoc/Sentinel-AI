# 🛡️ Sentinel AI

**Sentinel AI** is an AI-powered cybersecurity assistant designed to perform rapid website security assessments. It combines traditional security checks with AI-generated explanations to provide an easy-to-understand security report for websites and domains.

---

## Features

* 🌐 Website availability monitoring
* 🔒 SSL/TLS certificate inspection
* 🛡️ Security header analysis
* 🌍 Domain intelligence

  * Registrar
  * Domain age
  * Nameservers
* 🌐 DNS intelligence

  * A Records
  * MX Records
  * SPF validation
  * DMARC validation
* 🛜 Common port scanning
* 📊 Dynamic security risk scoring
* 🤖 AI-generated security analysis and recommendations
* ⚛️ React frontend dashboard
* ⚡ FastAPI backend

---

## Technology Stack

### Frontend

* React
* JavaScript
* CSS

### Backend

* FastAPI
* Python

### Libraries

* Requests
* python-whois
* dnspython
* python-nmap
* Uvicorn

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Tcodesoc/Sentinel-AI.git
cd Sentinel-AI
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn main:app --reload
```

Start the frontend:

```bash
npm install
npm run dev
```

---

## Example Scan

Scan any domain by typing:

```
scan github.com
```

Sentinel AI will generate a report including:

* Website status
* HTTPS status
* Security headers
* SSL certificate information
* Domain intelligence
* DNS intelligence
* Open ports
* Security score
* AI-powered security explanation

---

## Roadmap

Future enhancements include:

* CVE vulnerability lookup
* Service fingerprinting
* Technology detection
* WHOIS enhancements
* PDF report export
* User accounts
* Scan history
* Cloud deployment
* Threat intelligence integration

---

## Disclaimer

Sentinel AI is intended for educational purposes, defensive security testing, and authorized assessments only. Always obtain permission before scanning systems or networks that you do not own or administer.

---

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, submit pull requests, or open issues.

---

## Developer

Developed by **T-Codesoc**

GitHub:
https://github.com/Tcodesoc

---

## License

This project is licensed under the MIT License.
