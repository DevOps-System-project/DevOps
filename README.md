# DevOps and System Administration Service Delivery Project

## Deployment (Student 2)
1. Log in to the Linux VM using the `deploy` account and navigate to `/opt/devops-project`.
2. Load or verify the approved release image (`devops-info:v1.1.0` or `devops-info:<commit-sha>`):
   ```bash
   docker load < devops-info-<commit-sha>.tar.gz
   docker images --no-trunc devops-info:v1.1.0
   ```
3. Stop and remove any existing `devops-info` container before starting the new release:
   ```bash
   docker stop devops-info && docker rm devops-info
   docker run -d -p 8000:8000 --name devops-info devops-info:v1.1.0
   ```
   *Expected output:* Returns the 64-character container ID, and `docker ps` shows `devops-info` in `Up` status mapped to `0.0.0.0:8000->8000/tcp`.

## Health Check
Verify the `/health` endpoint responds with HTTP 200:
```bash
curl -i http://localhost:8000/health
```
*Expected output:*
```text
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 16

{"status":"ok"}
```

## Log Inspection
Inspect the last 50 lines of container output:
```bash
docker logs --tail 50 devops-info
```
*Expected output:*
```text
 * Serving Flask app 'main'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
172.17.0.1 - - [14/Nov/2026 17:37:58] "GET /health HTTP/1.1" 200 -
```
