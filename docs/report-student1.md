# Student 1 Report Sections: Application Architecture, Container Design, and Failure Recovery

**Author:** Halim Tayeb (Student 1 — Service & Container Lead)  
**Team Members:** Yazan Muhammed (Student 2 — Linux & Deployment Lead), Moayad Adel Alahmadi (Student 3 — CI/CD Lead)  
**Repository:** [https://github.com/DevOps-System-project/DevOps](https://github.com/DevOps-System-project/DevOps)  

---

## 1. Application Architecture & Service Design

### 1.1 Architectural Overview
The service is a lightweight, stateless HTTP microservice written in Python 3 using the Flask framework, with runtime dependencies pinned in `requirements.txt` (`flask==3.1.3`). The application exposes two HTTP routes and standard error handling:

1. **Information Route (`/`):**
   - Renders an HTML page presenting service metadata: service name (*Campus Help Desk*), contact email (*`support@example.com`*), operational hours (*Mon–Fri 08:00–17:00*), and the application version string (`VERSION = "1.1.0"`).
   - Designed without external database dependencies or dynamic state, ensuring deterministic startup and minimal runtime failure modes.
2. **Operational Health Probe (`/health`):**
   - Returns HTTP 200 with JSON payload: `{"status": "ok"}`.
   - Serves as the primary liveness and readiness probe for container health monitoring, deployment verification, and CI/CD smoke testing.
3. **Route Handling for Undefined Endpoints:**
   - Unmapped routes return HTTP 404, verified by automated unit tests in `tests/app/test_app_home_health_404.py`.

---

## 2. Containerization & Security Design

### 2.1 Base Image Selection & Footprint Minimization
The service container is defined in `Dockerfile` using the official `python:3.14-slim` base image. The `slim` variant omits heavy build dependencies, C compilers, and non-essential system tools present in full distribution images, substantially reducing the attack surface while maintaining full compatibility with the Python runtime.

### 2.2 Least Privilege Execution (Non-Root User)
By default, Docker containers execute processes under the root user (`UID 0`), creating significant privilege escalation risks if container isolation boundaries are compromised. To enforce the principle of least privilege:
- A dedicated unprivileged system account is created during image build: `RUN useradd --create-home appuser`.
- Dependencies are installed using layer-caching best practices: `COPY requirements.txt .` followed by `RUN pip install --no-cache-dir -r requirements.txt` occurs before copying source code (`COPY app/ app/`), ensuring package installation layers are reused when application code changes.
- Execution privileges are explicitly dropped using `USER appuser` prior to setting the entrypoint: `CMD ["python3", "-m", "app.main"]`.

### 2.3 Network Interface and Port Publishing
- **Internal Socket Binding:** Within the container, Flask binds to `0.0.0.0:8000`. By standard Docker bridge networking design, binding internally to `127.0.0.1` would isolate traffic strictly to the container's private network namespace, preventing the Docker port proxy (`docker-proxy`) on the host from forwarding inbound connections.
- **Host Port Publishing:** On developer machines, the container is published as `-p 127.0.0.1:8000:8000`, restricting exposure exclusively to the local loopback interface. On the deployment VM, the container was launched with `-p 8000:8000`, making port 8000 reachable across host interfaces; in conjunction with UFW rules allowing `8000/tcp` from `Anywhere`, this network exposure was formally identified and logged in the team risk register (`RISK-001` in `docs/records/risk-register.md`).

---

## 3. Operational Failure Recovery & Resilience

### 3.1 Controlled Failure Drill Analysis
To evaluate system observability and recovery procedures under operational failure, a controlled failure simulation was executed on the team Linux VM (recorded in `docs/evidence/failure-drill.txt`, PR #14):

1. **Baseline State:** Active container verified via `docker ps` and `curl -i http://localhost:8000/health` returning `HTTP/1.1 200 OK`.
2. **Failure Injection (14:09:21 UTC):** The service container was forcefully halted via `docker stop devops-info`.
3. **Symptom Detection:** Execution of `curl -i http://localhost:8000/health` immediately failed with `curl: (7) Failed to connect to localhost port 8000: Connection refused`.
4. **Recovery Execution (14:09:31 UTC):** The service was restarted using `docker start devops-info`.
5. **Restoration Verification (14:09:34 UTC):** Probing `/health` confirmed service restoration with `HTTP/1.1 200 OK`.
6. **Observed MTTR:** Total Mean Time to Recovery was measured at **13 seconds** (10 seconds detection and decision latency, 3 seconds container restart latency).

### 3.2 Recovery Automation & Future Hardening
The current deployment relies on manual operator intervention (`docker start`). For production resilience, container restart policies (`--restart unless-stopped` or `--restart on-failure`) or systemd-managed container units should be configured to eliminate operator intervention and reduce MTTR to sub-second container restart times.

---

## 4. Individual Reflection (Halim Tayeb)

### 4.1 Difficulty Encountered
During CI pipeline integration (PR #5), my initial test suite failed with a pytest `import file mismatch` error (commit `f7c7a15`). Both `tests/test_app.py` and `tests/app/test_app.py` shared identical base names across different subdirectories, triggering import collisions during pytest test discovery. Furthermore, during artifact verification, I observed that the local image configuration ID (`sha256:8db0f786...` from `build-info.txt`) matched my local container, but `sha256:70e46222...` recorded in `ci-runs.md` did not match the sha256 checksum of the downloaded archive (`d2b887...`).

### 4.2 Response & Resolution
I reviewed the CI run logs ([PR #5 Checks Run 132436899989](https://github.com/DevOps-System-project/DevOps/pull/5/checks?check_run_id=132436899989)), diagnosed the import collision, and renamed the test suite to a unique filename: `tests/app/test_app_home_health_404.py` (commit `5308774`), resolving the CI gate. For artifact verification, rather than assuming an unverified checksum, I authored PRs #11, #12, and #13 to document the exact facts: the CI pipeline exports a compressed archive rather than pushing to a registry, the image config ID matches `build-info.txt`, and the source of the `70e46222...` hash remains unverified.

### 4.3 Specific Next Improvement
In future workflows, I would implement an automated verification script that downloads release artifacts, executes `sha256sum`, unpacks `build-info.txt`, and cross-validates image configuration IDs and archive digests against pipeline metadata before any manual deployment.

---

## 5. References & Statement of AI Assistance

### 5.1 References
- **Flask Documentation Team.** (2024). *Flask Documentation (Version 3.1.x)*. Pallets Projects. https://flask.palletsprojects.com/
- **Docker Documentation Team.** (2024). *Dockerfile Best Practices & Non-Root Containers*. Docker Inc. https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- **Python Software Foundation.** (2024). *Python 3.14 Documentation & Standards*. https://docs.python.org/3/

### 5.2 Statement of AI Assistance
In accordance with academic integrity guidelines:
- **Tools Consulted:** Anthropic Claude and Google Antigravity (Gemini).
- **Scope of Usage:** AI assistants were consulted to analyze Git merge topologies, evaluate shell command diffs, draft initial text structure, and audit consistency between evidence files and markdown documentation.
- **Author Ownership:** All Python code (`app/main.py`), test cases (`tests/app/test_app_home_health_404.py`), Dockerfiles, and terminal commands were authored, executed, and verified by the student on live VM and repository environments.
