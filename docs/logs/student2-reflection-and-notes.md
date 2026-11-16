# Student 2 Individual Reflection & Technical Explanation

## 1. Individual Reflection
- **Personal Difficulty:** Coordinating repository history and Docker image traceability across teammates—specifically resolving unrelated Git root histories (`a573aa2` and `3dda96d`) and clarifying the difference between the CI artifact digest (`sha256:70e46222...`) and the unpacked Docker image config ID (`sha256:8db0f786...`).
- **Response:** Verified commit provenance via `git show`, cross-referenced both hashes in `docs/evidence/artifact-check.txt`, and documented an explicit traceability note in `docs/records/ci-runs.md`.
- **Specific Next Improvement:** Automate container startup with a systemd unit or Docker `--restart unless-stopped` policy so the service recovers automatically after a daemon or host reboot.

## 2. Technical Explanation Notes
- **Linux & Firewall Administration:** Configured named accounts (`yazan`, `halim`, `moayad`) and an unprivileged `deploy` owner for `/opt/devops-project`. Enforced default-deny incoming UFW rules allowing only `22/tcp` and `8000/tcp`, and verified service/disk health via `systemctl status docker`, `df -h`, and `docker ps`.
- **CI Pipeline Behavior:** Built `.github/workflows/ci.yml` on `pull_request` and `push` to `main` where `build-artifact` uses `needs: lint-and-test` (`flake8` and `pytest`), blocking artifact creation whenever static analysis or unit tests fail.
- **Artifact Traceability:** Linked every build to its GitHub Actions run ID, full commit SHA, image tag (`devops-info:<commit-sha>` / `v1.1.0`), and SHA256 digest across `docs/records/ci-runs.md` and `docs/deployment-checklist.md`.
- **Recovery Decisions:** Validated service failure detection (`curl: (7) Failed to connect`) and rapid container recovery (`docker start devops-info` restoring `HTTP/1.1 200 OK` on `/health` in 13 seconds) during the controlled failure simulation.
