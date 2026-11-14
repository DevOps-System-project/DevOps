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
├── app/
│   ├── __init__.py
│   └── main.py          # Flask application
├── docs/
│   └── evidence/        # Command output saved as proof
├── Dockerfile           # Container build instructions
├── requirements.txt     # Runtime dependency (flask==3.1.3)
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

- `http://127.0.0.1:8000/`: shows the service name, support contact, service hours, and version (`1.0.0`)
- `http://127.0.0.1:8000/health`: shows `{"status": "ok"}`

Stop the app with `Ctrl+C`.

## 2. Run with Docker

Build the image:

```bash
docker build -t devops-info:dev .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name devops-info devops-info:dev
```

Check that it is running:

```bash
docker ps
```

Expected: a row for `devops-info` with status `Up` and port `0.0.0.0:8000->8000/tcp`.

View the logs:

```bash
docker logs devops-info
```

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

Run the tests:

```bash
pytest tests/app
```

Run the linter:

```bash
flake8 app tests
```

## Notes

- The container runs as a non-root user (`appuser`).
- The app binds to `0.0.0.0` inside the container so that Docker can forward traffic to it, and to `127.0.0.1` when run locally.
- Evidence of each step is stored in `docs/evidence/`.
