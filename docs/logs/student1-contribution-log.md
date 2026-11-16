# Student 1 Contribution Log (Halim Tayeb, Service & Container lead)

## Pull requests authored

| PR | Branch | What it changed | CI evidence |
|---|---|---|---|
| [#4](https://github.com/DevOps-System-project/DevOps/pull/4) | `feature/readme-app` | Project README with setup instructions, Docker build/run, health check, test commands, and project structure | Passed CI checks on merge |
| [#5](https://github.com/DevOps-System-project/DevOps/pull/5) | `feature/app-tests` | Added `tests/app/test_app_home_health_404.py` (home page, `/health`, 404 tests) and `docs/evidence/ci-halim-runs.md` | Failed run `f7c7a15` (import mismatch), passing run `5308774` ([check run 132436899989](https://github.com/DevOps-System-project/DevOps/pull/5/checks?check_run_id=132436899989)) |
| [#8](https://github.com/DevOps-System-project/DevOps/pull/8) | `feature/artifact-check` | Initial `docs/evidence/artifact-check.txt` for v1.0.0 artifact verification | — |
| [#9](https://github.com/DevOps-System-project/DevOps/pull/9) | `feature/app-verify` | Added `docs/evidence/deploy-v1.0.0.txt` and `docs/evidence/app-verify.txt` for deployed version checks | — |
| [#10](https://github.com/DevOps-System-project/DevOps/pull/10) | `feature/version-1.1.0` | Bumped `VERSION` in `app/main.py` to `1.1.0` (commit `eb9c2a2`) | — |
| [#11](https://github.com/DevOps-System-project/DevOps/pull/11) | `feature/artifact-check-fix` | Corrected artifact-check.txt: documented image-to-tag gap (`3543571` built vs `382a24e` tagged) | — |
| [#12](https://github.com/DevOps-System-project/DevOps/pull/12) | `feature/artifact-check-cleanup` | Clarified archive-only pipeline (no registry push) and recorded exact `build-info.txt` `image_id` match | — |
| [#13](https://github.com/DevOps-System-project/DevOps/pull/13) | `feature/artifact-check-dedup` | Removed duplicate top section in `artifact-check.txt` caused by append instead of overwrite | — |

## Reviews

| PR | Author | My review | What I checked |
|---|---|---|---|
| [#3](https://github.com/DevOps-System-project/DevOps/pull/3) | Yazan | Approved with comments | UFW firewall rules, username sanitization, sudo justification |
| [#15](https://github.com/DevOps-System-project/DevOps/pull/15) | Yazan | Approved | Student 2 individual reflection and technical notes |
| [#16](https://github.com/DevOps-System-project/DevOps/pull/16) | Moayad | Approved | Student 3 weekly log, contribution log, reflection, and CI traceability improvement record; cross-checked commit hashes and run IDs against `git log` |

## Still to complete

- Controlled failure drill on the VM (docker stop / docker start with timed recovery).
- Student 1 report sections (Architecture, Container Design, Failure Recovery, Reflection, AI Disclosure).

## Assistance disclosure

I used an AI assistant (Antigravity / Gemini) to help draft documentation, check evidence consistency, and review PRs. I ran all commands, verified all outputs, and I am responsible for explaining them.
