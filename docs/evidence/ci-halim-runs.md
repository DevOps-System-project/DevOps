# CI Runs for feature/app-tests (Student 1: Halim Tayeb)

## Run 1: Failed
- Commit: f7c7a15
- Result: Static check and tests FAILED
- Cause: pytest "import file mismatch". Two files were both named test_app.py (tests/app/ and tests/).
- Run link: https://github.com/DevOps-System-project/DevOps/pull/5/checks?sha=f7c7a15591567437545455df2b291774fcf897ad

## Run 2: Passed
- Commit: 5308774 ("Rename app tests to a unique file name for pytest")
- Result: All checks passed. 8 tests passed.
- Fix: renamed tests/app/test_app.py to tests/app/test_app_home_health_404.py
- Run link: https://github.com/DevOps-System-project/DevOps/pull/5/checks?check_run_id=132436899989
