# Service Deployment Checklist

Maintained by: Student 2 (`yazan` / GitHub: `@Link-rm-rf`)
Target Environment: Isolated Linux VM (`172.25.222.233/20`, `/opt/devops-project`)
Service Account: `deploy` (Non-sudo, member of `docker` group)

---

## 1. Prerequisites
- [ ] Target Linux VM is reachable on the private lab network (`172.25.222.233`) and UFW rules allow ports `22/tcp` and `8000/tcp`.
- [ ] Docker daemon (`docker.service`) is active and running (`systemctl status docker`).
- [ ] Sufficient disk space is available on `/` (`df -h` shows < 80% usage).
- [ ] Pull Request has been peer-reviewed, approved by at least one teammate, and merged into `main`.
- [ ] GitHub Actions CI workflow (`lint-and-test` and `build-artifact`) completed with status `success`.

## 2. Approval
- **Release v1.0.0:**
  - **Approver:** Student 1 (`@halimtayeb47`) & Student 2 (`@Link-rm-rf`)
  - **Change Record:** `docs/records/change-record-001.md`
  - **Approval Status:** Approved for VM deployment

## 3. Artifact Identifier
- **Release v1.0.0:**
  - **Source Commit SHA:** `35435717c01dda274a7b35b8101b76a41f5e2634`
  - **CI Workflow Run ID:** `43596029502`
  - **Container Image Tag:** `devops-info:35435717c01dda274a7b35b8101b76a41f5e2634`
  - **Image ID / Digest:** `sha256:70e46222bbd724bec1a1123dad0c3120af002571737254feda97ca2116ff1205`

## 4. Deployment Steps
1. Log into the Linux VM using the dedicated least-privilege deployment account:
   ```bash
   su - deploy
   cd /opt/devops-project
   ```
2. Load or pull the verified release image built for the target commit SHA:
   ```bash
   # If loading from the CI artifact archive:
   docker load < devops-info-<commit-sha>.tar.gz
   # Verify image tag and digest match release metadata:
   docker images --no-trunc devops-info:<commit-sha>
   ```
3. If an existing `devops-info` container is running (e.g., when upgrading from `v1.0.0` to `v1.1.0`), record the stop timestamp and remove the old container:
   ```bash
   date -u +"%Y-%m-%d %H:%M:%S UTC"
   docker stop devops-info && docker rm devops-info
   ```
4. Start the new container bound to port `8000`:
   ```bash
   docker run -d -p 8000:8000 --name devops-info devops-info:<commit-sha>
   ```
5. Confirm container status is `Up`:
   ```bash
   docker ps --filter "name=devops-info"
   ```

## 5. Health Check
1. Query the `/health` endpoint and verify HTTP `200 OK` and JSON body `{"status":"ok"}`:
   ```bash
   curl -i http://localhost:8000/health
   ```
2. Query the main service page (`/`) and verify the displayed `Version:` matches the target release (`1.0.0` or `1.1.0`):
   ```bash
   curl -s http://localhost:8000/
   ```
3. Save all verification outputs to `docs/evidence/deploy-v1.0.0.txt` (or `docs/evidence/deploy-v1.1.0.txt`).

## 6. Rollback Steps
If the health check fails or the deployed version exhibits unexpected errors:
1. Record the failure timestamp and current container state (`docker ps`, `docker logs --tail 50 devops-info`).
2. Stop and remove the faulty container:
   ```bash
   docker stop devops-info && docker rm devops-info
   ```
3. Start the previous known-good release image (`v1.0.0` — `devops-info:35435717c01dda274a7b35b8101b76a41f5e2634`):
   ```bash
   docker run -d -p 8000:8000 --name devops-info devops-info:35435717c01dda274a7b35b8101b76a41f5e2634
   ```
4. Re-run the health and version checks (`curl -i http://localhost:8000/health` and `curl -s http://localhost:8000/`) and record the total recovery time.
