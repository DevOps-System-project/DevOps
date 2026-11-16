# Student 2 Weekly Work Log
| Date | Task Planned | Task Completed | Evidence Link / File | Problem Encountered | Next Action |
|---|---|---|---|---|---|
| 10/11/2026 | VM setup, accounts, snapshot, GitHub repo & branch rules | Created VM accounts, `before-project` snapshot, repo & `main` protection | `docs/linux-configuration.md`, `docs/evidence/linux-checks.txt` | None | Create `.gitignore`, PR template, and CI skeleton |
| 11/11/2026 | Repo rules & CI workflow start | Added `.gitignore`, PR template, `.github/workflows/ci.yml`, opened PR | `.github/pull_request_template.md`, `.github/workflows/ci.yml` | None | Configure UFW firewall and review teammate PR |
| 12/11/2026 | Firewall rules & peer review | Configured UFW (SSH + port 8000), connectivity test, reviewed PR | `docs/linux-configuration.md` | None | Add lint/test CI jobs and run failure test |
| 13/11/2026 | CI lint/test jobs & failed run test | Configured `flake8`, `pytest`, job dependencies, recorded failed/passing runs | `docs/records/ci-runs.md` | Intentional test failure verified pipeline gate | Deploy `v1.0.0` and `v1.1.0` |
| 14/11/2026 | Deploy `v1.0.0` & `v1.1.0` | Created deployment checklist, deployed both releases, verified `/health` | `docs/deployment-checklist.md`, `docs/evidence/deploy-v1.0.0.txt`, `docs/evidence/deploy-v1.1.0.txt` | None | Collect ops evidence and support failure drill |
| 15/11/2026 | Ops evidence & failure drill | Collected `docker ps`, logs, `df -h`, service status, and failure drill timestamps | `docs/evidence/ops-status.txt`, `docs/evidence/ops-logs.txt`, `docs/evidence/failure-drill.txt` | Container stopped after daemon restart; restarted and verified | Complete README, report sections, logs, and freeze work |
| 16/11/2026 | Documentation, instructor update & freeze | Wrote README deployment/health/logs sections, report sections, and personal logs | `README.md`, `docs/report-student2.md`, `docs/logs/` | None | Buffer check on 17/11 and final submission confirmation |
