# Improvement record: artifact linked to the real source commit

Owner: Moayad Alahmadi (Student 3). Change: [PR #6](https://github.com/DevOps-System-project/DevOps/pull/6).

## Weakness (with evidence)

On pull requests the pipeline named the saved image after `github.sha`. For a pull request that value is GitHub's temporary merge commit, not the commit the author pushed.

- PR #1, [run 43213285328](https://github.com/DevOps-System-project/DevOps/actions/runs/43213285328): the PR head commit was `7187870`, but the artifact was saved as `devops-info-dc1fe30cef7e220a4209ecfe32512054ea55bf53`. Commit `dc1fe30` is not in the repository history, so the artifact could not be traced to its source.
- Release images were named only by commit SHA, so a version such as `v1.0.0` could not be found by name.

## Change

PR #6 changed `.github/workflows/ci.yml`:

- `SOURCE_SHA: ${{ github.event.pull_request.head.sha || github.sha }}`: the real source commit on pull requests and pushes.
- The image is tagged with both the version (on `v*` tags) and the full source commit, and both are written to `build-info.txt`.
- On a tag, the pipeline stops if the tag does not match `VERSION` in `app/main.py`.

## After (repeat of the check)

- PR #6, [run 43597279483](https://github.com/DevOps-System-project/DevOps/actions/runs/43597279483): head commit `f927fc2`, artifact `devops-info-sha-f927fc2`. The name now matches the source commit.
- Tag `v1.1.0`, [run 43621860384](https://github.com/DevOps-System-project/DevOps/actions/runs/43621860384): image `devops-info:v1.1.0`, `build-info.txt` records `source_commit=967d965…` (the commit the tag points to) and `image_id=sha256:fb060f5f…`.

## Limits

- No speed or reliability gain is claimed; the improvement is traceability.
- `v1.0.0` was deployed before this change, so it is identified by its commit-SHA image (`3543571`), and its tag was later re-created on `382a24e` (see `docs/evidence/artifact-check.txt`).
