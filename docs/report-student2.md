# Student 2 Report Sections: Linux Environment, Git Workflow, and CI

## 1. Linux Virtual Machine & Firewall Configuration
- **Environment:** Isolated Linux VM configured with named user accounts (`yazan`, `halim`, `moayad`) and a restricted `deploy` account owning `/opt/devops-project`.
- **Firewall Rules:** Only SSH from the private lab network and application port `8000/tcp` are open; all other incoming traffic is denied by default.

## 3. Firewall Rules (`sudo ufw status numbered`)
    Status: active

         To                         Action      From
         --                         ------      ----
    [ 1] 22/tcp                     ALLOW IN    Anywhere                  
    [ 2] 8000/tcp                   ALLOW IN    Anywhere                  
    [ 3] 22/tcp (v6)                ALLOW IN    Anywhere (v6)             
    [ 4] 8000/tcp (v6)              ALLOW IN    Anywhere (v6)             

> **Security Note on Network Scope:** While the WSL2 virtual interface (`172.25.222.233/20`) resides behind a NATed host-only virtual switch not routable from external networks, UFW rules `[1]`–`[4]` currently permit `22/tcp` and `8000/tcp` from `Anywhere` within the virtual interface scope. This wider rule scope is logged in `docs/records/risk-register.md` (Risk ID: `RISK-001`) with a mitigation action to restrict `22/tcp` explicitly to the `172.25.208.0/20` lab CIDR if the VM remains in extended use.

## 2. Git Workflow & Branch Protection
- **Branching Model:** Direct pushes to `main` are blocked; all changes enter via `feature/*` or `docs/*` branches using `.github/pull_request_template.md`.
- **Branch Protection Settings on `main`:**
  - Require a pull request before merging (minimum 1 approving peer review).
  - Require status checks to pass before merging (`lint` and `test` CI jobs).

## 3. Continuous Integration (CI) Pipeline
- Defined in `.github/workflows/ci.yml` triggered on `pull_request` and `push` to `main`.
- **Jobs:** `lint` (`flake8 app/ tests/`) and `test` (`pytest tests/app/`) run first; the `artifact` job depends on both (`needs: [lint, test]`), blocking image creation if either fails.

## 4. Operations & Normal Log Line Explanation
- **Normal Log Line:** `172.17.0.1 - - [14/Nov/2026 17:37:58] "GET /health HTTP/1.1" 200 -`
  - `172.17.0.1`: Docker bridge gateway IP sending the health check request.
  - `[14/Nov/2026 17:37:58]`: Timestamp when the server processed the request.
  - `"GET /health HTTP/1.1"`: HTTP method, requested endpoint, and protocol version.
  - `200`: HTTP status code confirming the application responded healthy.
