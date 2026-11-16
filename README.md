# DevOps Service Delivery Project

A small Python web service that shows a fictional service information page and exposes a `/health` endpoint. It runs locally with Flask and in a Docker container.

## Requirements

- Python 3 (tested with Python 3.14.4)
- Git
- Docker (tested with Docker 29.1.3)
- `curl` for the health check

## Project Structure

```
devops-team-project/
├── .flake8                              # flake8 lint configuration
├── .gitignore                           # excludes .venv, __pycache__, .env
├── .github/
│   ├── pull_request_template.md         # PR template
│   └── workflows/
│       └── ci.yml                       # GitHub Actions CI pipeline
├── app/
│   ├── __init__.py
│   └── main.py                          # Flask app (VERSION, /, /health)
├── docs/
│   ├── deployment-checklist.md          # Deployment steps and rollback
│   ├── linux-configuration.md           # VM specs, accounts, firewall rules
│   ├── evidence/
│   │   ├── app-verify.txt               # Deployed version check
│   │   ├── artifact-check.txt           # v1.0.0 artifact verification
│   │   ├── ci-halim-runs.md             # Failed and passing CI run links
│   │   ├── connectivity-check.txt
│   │   ├── container-check.txt
│   │   ├── deploy-v1.0.0.txt
│   │   ├── linux-checks.txt
│   │   └── readme-log-halim.txt         # Container log capture
│   └── records/
│       ├── ci-runs.md
│       ├── risk-register.md
│       └── work-log-yazan.md
├── tests/
│   ├── app/
│   │   └── test_app_home_health_404.py  # Home, /health, and 404 tests
│   └── test_app.py                      # Shared app tests
├── Dockerfile                           # Container build instructions
├── requirements.txt                     # Runtime dependency (flask==3.1.3)
├── requirements-dev.txt                 # Dev dependencies (pytest, flake8)
└── README.md
```

## 1. Run Locally

Run these commands from the project root.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependency:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python3 -m app.main
```

Expected output includes:

```
* Running on http://127.0.0.1:8000
```

Open these URLs in a browser:

- `http://127.0.0.1:8000/` shows the service name, support contact, service hours, and version (`1.0.0`).
- `http://127.0.0.1:8000/health` shows `{"status": "ok"}`.

Stop the app with `Ctrl+C`.

## 2. Run with Docker

Build the image:

```bash
docker build -t devops-info:dev .
```

Run the container, publishing the port only on the host's localhost:

```bash
docker run -d -p 127.0.0.1:8000:8000 --name devops-info devops-info:dev
```

Check that it is running:

```bash
docker ps
```

Expected: a row for `devops-info` with status `Up` and port `127.0.0.1:8000->8000/tcp`.

Check the logs. See Section 6 (Production Health Check & Log Inspection).

Stop and remove the container when finished:

```bash
docker stop devops-info
docker rm devops-info
```

## 3. Health Check

With the container running, run:

```bash
curl http://localhost:8000/health
```

Expected output:

```json
{"status":"ok"}
```

## 4. Tests and Linting

Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the tests (this is the same command the CI pipeline runs):

```bash
python -m pytest -v
```

Run the linter:

```bash
flake8 app tests
```

## 5. Notes

- The container runs as a non-root user (`appuser`).
- The app listens on `0.0.0.0:8000` inside the container, and the Docker command above publishes it only on `127.0.0.1` of the host.
- The app binds to `127.0.0.1` when run locally with `python3 -m app.main`.
- Evidence of each step is stored in `docs/evidence/`.

## 6. Production Health Check & Log Inspection

On the team VM, the container is published on all interfaces (`-p 8000:8000`), which is recorded as risk RISK-001 in `docs/records/risk-register.md`. Replace `<VM-address>` with the VM's address.

Check the health endpoint from another machine:

```bash
curl -i http://<VM-address>:8000/health
```

Inspect the last 50 lines of container output:

```bash
docker logs --tail 50 devops-info
```

Observed output (from `docs/evidence/readme-log-halim.txt`, captured on the VM):

```text
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
172.17.0.1 - - [11/Nov/2026 06:38:53] "GET /health HTTP/1.1" 200 -
172.17.0.1 - - [11/Nov/2026 06:41:47] "GET /health HTTP/1.1" 200 -
172.17.0.1 - - [11/Nov/2026 06:42:02] "GET /health HTTP/1.1" 200 -
172.17.0.1 - - [14/Nov/2026 14:36:56] "GET /health HTTP/1.1" 200 -
172.17.0.1 - - [14/Nov/2026 14:36:56] "GET / HTTP/1.1" 200 -
 * Serving Flask app 'main'
 * Debug mode: off
```

`docker logs` shows the server startup output, the bind addresses, and one entry per incoming request. Each request line gives the client IP (`172.17.0.1`, the Docker bridge gateway for requests forwarded from the host), the timestamp, the HTTP method and path, the status code (`200` means success), and the response size (shown as `-` in this setup). The timestamps come from the VM capture and span more than one run.
