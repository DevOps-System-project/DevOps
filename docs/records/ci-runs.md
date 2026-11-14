# CI Pipeline Runs and Artifact Traceability Record

Maintained by: Student 2 (`yazan` / GitHub: `@Link-rm-rf`)

## 1. Deliberate Failure and Fix Verification (Day 4)

The pipeline enforces a strict quality gate: `build-artifact` specifies `needs: lint-and-test`, ensuring no container image or artifact is built when linting (`flake8`) or unit testing (`pytest`) fails.

| Run Type | Workflow Run ID | Commit SHA | Status / Conclusion | Evidence Link | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Static Check Failure** | `43213092502` | `6876b3380da884cb09352e78e60f19624e5f270f` | Failed (`failure`) | [Run 43213092502](https://github.com/DevOps-System-project/DevOps/actions/runs/43213092502) | `flake8` caught trailing blank line (`W391`); `build-artifact` job was skipped. |
| **Static Check Fix** | `43213285328` | `7187870ad4d2860b869a2fda3f3b9d614ead08c2` | Passed (`success`) | [Run 43213285328](https://github.com/DevOps-System-project/DevOps/actions/runs/43213285328) | Removed trailing blank line in `app/main.py`; all checks and artifact build passed. |
| **Deliberate Test Failure** | `43591073438` | `f7c7a15591567437545455df2b291774fcf897ad` | Failed (`failure`) | [Run 43591073438](https://github.com/DevOps-System-project/DevOps/actions/runs/43591073438) | Deliberate failing test assertion in `tests/test_app.py`; pipeline halted and blocked artifact creation. |
| **Restored Test Fix** | `43591466744` | `530877416760044426c8eba099a740ff89e15453` | Passed (`success`) | [Run 43591466744](https://github.com/DevOps-System-project/DevOps/actions/runs/43591466744) | Restored expected assertion; `pytest` passed (3/3) and `build-artifact` published the image archive. |

## 2. Release Artifact Builds on `main` (Day 5)

| Release Version | Workflow Run ID | Commit SHA | Image Tag | Image Digest / ID | Pipeline Run URL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **v1.0.0** | `43596029502` | `35435717c01dda274a7b35b8101b76a41f5e2634` | `devops-info:35435717c01dda274a7b35b8101b76a41f5e2634` | `sha256:70e46222bbd724bec1a1123dad0c3120af002571737254feda97ca2116ff1205` | [Run 43596029502](https://github.com/DevOps-System-project/DevOps/actions/runs/43596029502) |
