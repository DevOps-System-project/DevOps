DevOps Service Delivery Project
A small Python web service that shows a fictional service information page and exposes a /health endpoint. It runs locally with Flask and in a Docker container.

Requirements
Python 3 (tested with Python 3.14.4)

Git

Docker (tested with Docker 29.1.3)

curl for the health check

Project Structure
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
│   │   ├── ci-halim-runs.md             # Failed and passing CI run links
│   │   ├── connectivity-check.txt
│   │   ├── container-check.txt
│   │   ├── deploy-v1.0.0.txt
│   │   └── linux-checks.txt
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
1. Run Locally
Run these commands from the project root.

Create and activate a virtual environment:

Bash
python3 -m venv .venv
source .venv/bin/activate
Install the dependency:

Bash
pip install -r requirements.txt
Start the app:

Bash
python3 -m app.main
Expected output includes:

- Running on http://127.0.0.1:8000
Open these URLs in a browser:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/) shows the service name, support contact, service hours, and version (1.0.0).

[http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) shows {"status": "ok"}.

Stop the app with Ctrl+C.

2. Run with Docker
Build the image:

Bash
docker build -t devops-info:dev .
Run the container, publishing the port only on the host's localhost:

Bash
docker run -d -p 127.0.0.1:8000:8000 --name devops-info devops-info:dev
Check that it is running:

Bash
docker ps
Expected: a row for devops-info with status Up and port 127.0.0.1:8000->8000/tcp.

View the logs:

Bash
docker logs devops-info
Stop and remove the container when finished:

Bash
docker stop devops-info
docker rm devops-info
3. Health Check
With the container running, run:

Bash
curl http://localhost:8000/health
Expected output:

JSON
{"status":"ok"}
4. Tests and Linting
Install the development dependencies:

Bash
pip install -r requirements-dev.txt
Run the tests (this is the same command the CI pipeline runs):

Bash
python -m pytest -v
Run the linter:

Bash
flake8 app tests
5. Deployment (Student 2)
Log in to the Linux VM using the deploy account and navigate to /opt/devops-project.

Load or verify the approved release image (devops-info:v1.1.0 or devops-info:<commit-sha>):

Bash
docker load < devops-info-<commit-sha>.tar.gz
docker images --no-trunc devops-info:v1.1.0
Stop and remove any existing devops-info container before starting the new release:

Bash
docker stop devops-info && docker rm devops-info
docker run -d -p 8000:8000 --name devops-info devops-info:v1.1.0
Expected output: Returns the 64-character container ID, and docker ps shows devops-info in Up status mapped to 0.0.0.0:8000->8000/tcp.

6. Production Health Check & Log Inspection
Verify the deployed /health endpoint responds with HTTP 200:

Bash
curl -i http://localhost:8000/health
Expected output:

Plaintext
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 16

{"status":"ok"}
Inspect the last 50 lines of container output:

Bash
docker logs --tail 50 devops-info
Expected output:

Plaintext
 * Serving Flask app 'main'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
172.17.0.1 - - [14/Nov/2026 17:37:58] "GET /health HTTP/1.1" 200 -
Notes
The container runs as a non-root user (appuser).

The app listens on 0.0.0.0:8000 inside the container, and the Docker command publishes it only on 127.0.0.1 of the host.

The app binds to 127.0.0.1 when run locally with python3 -m app.main.

Evidence of each step is stored in docs/evidence/.