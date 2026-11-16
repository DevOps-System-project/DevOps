# Student 3 Contribution Log (Moayad Alahmadi, CI lead)

## Pull requests authored

| PR | Branch | What it changed | CI evidence |
|---|---|---|---|
| [#1](https://github.com/DevOps-System-project/DevOps/pull/1) | `feature/ci-tests` | Added `tests/test_app.py` (home page content, `/health`, 404, POST to `/health` refused, version format), `requirements-dev.txt`, `.flake8`, and `.github/workflows/ci.yml`. The build job has `needs: lint-and-test`, so a failed check blocks the image. | Failed [run 43213092502](https://github.com/DevOps-System-project/DevOps/actions/runs/43213092502) (flake8 `W391`), fix `7187870`, passing [run 43213285328](https://github.com/DevOps-System-project/DevOps/actions/runs/43213285328) |
| [#6](https://github.com/DevOps-System-project/DevOps/pull/6) | `feature/release-tags` | Pipeline also runs on `v*` tags; image tagged `devops-info:<version>` and `devops-info:<source SHA>`; tag must match `VERSION` in `app/main.py`; uses the PR head commit instead of GitHub's temporary merge commit; attaches the image archive and `build-info.txt` to the release; `contents: write` only on the build job. | [run 43597279483](https://github.com/DevOps-System-project/DevOps/actions/runs/43597279483); used for `v1.1.0` in [run 43621860384](https://github.com/DevOps-System-project/DevOps/actions/runs/43621860384) |

Commits on `main` that changed `.github/workflows/ci.yml`: `6876b33` and `f927fc2` (both mine).

## Reviews

| PR | Author | My review | What I checked |
|---|---|---|---|
| [#5](https://github.com/DevOps-System-project/DevOps/pull/5) | Halim | Approved | Ran `python -m pytest -v` (8 passed) and `flake8`; noted `pytest tests/app` fails on import |
| [#4](https://github.com/DevOps-System-project/DevOps/pull/4) | Halim | Changes requested (twice), then approved | README test command failed; port binding note wrong; project tree pasted three times; re-ran the final commands (8 passed) |
| [#7](https://github.com/DevOps-System-project/DevOps/pull/7) | Yazan | Approved | Deployment records for `v1.0.0` |
| [#11](https://github.com/DevOps-System-project/DevOps/pull/11) | Halim | Approved with notes | Image ID vs digest, and no registry in the pipeline; led to the image-ID match recorded in PRs #12 and #13 |
| [#14](https://github.com/DevOps-System-project/DevOps/pull/14), [#15](https://github.com/DevOps-System-project/DevOps/pull/15) | Yazan | Approved | Student 2 documentation |

## Releases and operation

- Created release [`v1.0.0`](https://github.com/DevOps-System-project/DevOps/releases) on commit `3543571`, the source of the deployed image (14/11/2026). A teammate later re-created the tag on `382a24e`; the gap is recorded in `docs/evidence/artifact-check.txt`.
- My pipeline built and published release `v1.1.0` from its tag ([run 43621860384](https://github.com/DevOps-System-project/DevOps/actions/runs/43621860384)).
- Process improvement: see `docs/records/improvement-ci-traceability.md`.

## Linux administration and recovery

- Linux checks on my own lab VM (Ubuntu 26.04.1): account and groups, disk usage, home directory permissions, Docker version and service state. Evidence: `docs/evidence/linux-checks-moayad.txt`.
- Rollback drill from `v1.1.0` to `v1.0.0` using the CI-built artifacts (loaded, not rebuilt; both image IDs match their `build-info.txt`). Version 1.0.0 displayed and `/health` returned 200 OK. Measured recovery time 12.1 s, under QEMU emulation. Evidence: `docs/evidence/rollback-v1.0.0-moayad.txt`.
- Not yet done on the team VM; planned for the final demonstration.
