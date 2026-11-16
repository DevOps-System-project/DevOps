# DevOps Service Delivery Project

A small Python web service that displays fictional service information and provides a `/health` endpoint for monitoring service availability.

The application runs locally using Flask and can also be built and deployed as a Docker container. The project includes automated testing, linting, and a GitHub Actions CI pipeline.

## Requirements

The following tools are required to run and test the project:

- **Python 3** (tested with Python 3.14.4)
- **Git**
- **Docker** (tested with Docker 29.1.3)
- **curl** (for health checks)

## Project Structure

```text
devops-team-project/
├── .flake8
├── .gitignore
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── docs/
│   ├── deployment-checklist.md
│   ├── linux-configuration.md
│   ├── evidence/
│   │   ├── ci-halim-runs.md
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
│   │   └── test_app_home_health_404.py
│   └── test_app.py
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## 1. Running the Application Locally

Run all commands from the project root directory.

### Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
python3 -m app.main
```

The application should start at:

```text
http://127.0.0.1:8000
```

Open the following URLs in your browser:

- **Home page:** http://127.0.0.1:8000/

  Displays the service name, support contact, service hours, and application version (1.0.0).

- **Health endpoint:** http://127.0.0.1:8000/health

  Returns the following JSON response:

```json
{"status": "ok"}
```

To stop the application, press `Ctrl+C`.

## 2. Running the Application with Docker

### Build the Docker image

From the project root, run:

```bash
docker build -t devops-info:dev .
```

### Start the container

```bash
docker run -d -p 127.0.0.1:8000:8000 --name devops-info devops-info:dev
```

The application will be accessible through port 8000 on the local host.

### Verify the container

```bash
docker ps
```

Expected result: A running container named `devops-info` with the following port mapping:

```text
127.0.0.1:8000->8000/tcp
```

### View container logs

```bash
docker logs devops-info
```

### Stop and remove the container

```bash
docker stop devops-info
docker rm devops-info
```

## 3. Health Check

With the Docker container running, execute:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{"status":"ok"}
```

This confirms that the application is running and its health endpoint is responding correctly.

## 4. Testing and Linting

The project includes automated tests using pytest and code-quality checks using Flake8.

### Install development dependencies

```bash
pip install -r requirements-dev.txt
```

### Run automated tests

```bash
python -m pytest -v
```

This executes the project's test suite, including checks for:

- Home page response.
- Health endpoint response.
- Handling of non-existent routes (404).

The same test command is used by the GitHub Actions CI pipeline.

### Run code linting

```bash
flake8 app tests
```

This checks the application and test files for code-quality and formatting issues.

## 5. Deployment (Student 2)

The application is deployed to a Linux virtual machine using the designated deployment account.

### Access the deployment directory

Log in to the Linux VM using the deployment account and navigate to:

```bash
cd /opt/devops-project
```

### Load or verify the approved Docker image

Load the exported Docker image if it has not already been loaded:

```bash
docker load < devops-info-COMMIT_SHA.tar.gz
```

Verify that the approved release image is available:

```bash
docker image inspect devops-info:v1.1.0
```

The approved release image can use either the `devops-info:v1.1.0` tag or the corresponding commit SHA tag.

### Replace the existing container

Stop and remove the previous container before deploying the new release:

```bash
docker stop devops-info && docker rm devops-info
```

### Start the new release

```bash
docker run -d -p 8000:8000 --name devops-info devops-info:v1.1.0
```

Expected result:

- Docker returns a 64-character container ID.
- The container appears in `docker ps` with an `Up` status.
- Port 8000 is mapped to `0.0.0.0:8000` on the host.

## 6. Production Health Check and Log Inspection

After deployment, verify that the application is accessible and responding correctly.

### Check the health endpoint

```bash
curl -i http://localhost:8000/health
```

Expected response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 16

{"status":"ok"}
```

The HTTP 200 status confirms that the health endpoint is responding successfully.

### Inspect container logs

```bash
docker logs --tail 50 devops-info
```

Expected output includes:

```text
* Serving Flask app 'main'
* Debug mode: off
* Running on all addresses (0.0.0.0)
172.17.0.1 - - [14/Nov/2026 17:37:58] "GET /health HTTP/1.1" 200 -
```

The logs provide information about application startup and incoming requests.

## 7. Additional Notes

- The Docker container runs as a non-root user named `appuser`.
- Inside the container, the application listens on `0.0.0.0:8000`.
- When running locally with `python3 -m app.main`, the application binds to `127.0.0.1:8000`.
- The local Docker configuration publishes the application only on the host's localhost interface.
- The production deployment publishes the application on port 8000 of the Linux VM.
- The project uses GitHub Actions for continuous integration, including automated tests and linting.
- The `.gitignore` file excludes temporary files and sensitive local configuration, including `.venv`, `__pycache__`, and `.env`.

## 8. Project Documentation and Evidence

Additional project documentation and execution evidence are available in the `docs/` directory.

| Directory / File | Description |
|---|---|
| `docs/deployment-checklist.md` | Deployment procedures and rollback steps |
| `docs/linux-configuration.md` | Linux VM specifications, accounts, and firewall rules |
| `docs/evidence/` | Evidence of CI, connectivity, container, and deployment checks |
| `docs/records/ci-runs.md` | CI execution records |
| `docs/records/risk-register.md` | Project risk assessment |
| `docs/records/work-log-yazan.md` | Individual work log |

These files provide supporting documentation and evidence of the project's implementation, testing, and deployment activities.
