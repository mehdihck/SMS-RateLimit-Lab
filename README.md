<div align="center">

# SMS Rate Limit Lab

### Controlled OTP Rate-Limiting & Header-Trust Research

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Lab](https://img.shields.io/badge/Environment-Local%20Only-00AEEF?style=for-the-badge)](#safety)
[![Security Research](https://img.shields.io/badge/Focus-Application%20Security-172554?style=for-the-badge)](#)

**MEHDIHCK · Learn. Build. Test. Secure.**

</div>

---

## Overview

SMS Rate Limit Lab is a local-only Python demonstration environment for studying OTP request throttling, HTTP `429 Too Many Requests` behavior, and the security implications of trusting client-supplied forwarding headers.

The project uses a deterministic in-process simulator. It does **not** send SMS messages, contact a third-party API, or generate traffic to external systems.

## Research goals

- Observe how a per-client request limit behaves.
- Compare a limiter that trusts a client-supplied identity header with one that uses a server-controlled identity.
- Verify that a blocked client receives a simulated `429` response.
- Produce repeatable local test results.

## Safety

This repository is intentionally restricted to local simulation. Do not adapt it to send OTP requests to real services or use it to bypass another system's protections. Only test systems for which you have explicit written authorization and within the approved scope.

The original live-target scripts are not included in this public repository. Keep raw evidence, target identifiers, phone numbers, credentials, and any client-confidential material private. Publish a sanitized report only if your authorization permits disclosure.

## Project structure

```text
SMS-RateLimit-Lab/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── rate_limiter.py
│   └── simulator.py
├── tests/
│   ├── __init__.py
│   └── test_rate_limit.py
└── reports/
    └── sample-report.md
```

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Run the local demonstration

```bash
python -m src.simulator
```

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

## What the demonstration shows

The simulator runs two isolated examples:

1. **Header-trusting configuration:** the demonstration shows why a server should not treat an arbitrary client-provided `X-Forwarded-For` value as verified identity.
2. **Server-identity configuration:** the limiter uses a server-controlled client identifier, so changing a request header does not create a new identity.

All requests are in-memory objects. No HTTP client or network connection is used.

## Interpreting results

A simulated `429` means the local limiter rejected a request after the configured quota was reached. It is not evidence that any external service is vulnerable. Real deployments should enforce limits at trusted infrastructure boundaries and should only honor forwarding headers from explicitly trusted proxies.

## Research report

See [`reports/sample-report.md`](reports/sample-report.md) for a report template. Replace placeholders only with findings that are supported by authorized evidence and approved for public disclosure.

## Author

**MEHDIHCK**  
Python · Django · Application Security

[GitHub profile](https://github.com/mehdihck)

---

<div align="center">

`UNDERSTAND THE CONTROL. TEST SAFELY. REPORT RESPONSIBLY.`

</div>
