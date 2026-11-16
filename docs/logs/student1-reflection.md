# Student 1 Individual Reflection (Halim Tayeb)

## Difficulty

I was responsible for the service application and its containerization. The biggest challenge was artifact traceability: when I downloaded the CI artifact and checked the image ID against the pipeline record, I found that `sha256:8db0f786...` (the Docker image config ID in `build-info.txt`) matched my local image, but `sha256:70e46222...` (recorded in `ci-runs.md`) did not match the `sha256sum` of the downloaded archive (`d2b887...`). I had to document this gap honestly rather than claim a match that did not exist.

## How I responded

- I kept the discrepancy visible in `docs/evidence/artifact-check.txt` across PRs #11, #12, and #13, each refining the explanation: the pipeline exports an archive (no registry push), the image config ID matches `build-info.txt`, and the source of `70e46222...` is unverified.
- For the README log section, my first `docker logs` redirect captured only stdout (2 lines). I learned that Flask writes request logs to stderr, so I recaptured with `2>&1` and got the full 19-line output. I copied it verbatim into the README rather than editing it.
- PR #4 (the README) was rejected twice by Moayad for a broken test command, wrong port binding note, and a triple-pasted project tree. I fixed each issue in separate commits and learned to run every command in the README before submitting.

## Next improvement

The evidence file `docs/evidence/artifact-check.txt` records the image ID match but not the archive checksum mismatch in a machine-readable way. A future improvement would be a script that downloads the CI artifact, runs `sha256sum`, extracts `build-info.txt`, and compares both values automatically, failing the check if either does not match a known record.

## Assistance disclosure

I used an AI assistant (Antigravity / Gemini) to help draft documentation, structure the README, review evidence consistency, and prepare PR review comments. I ran all terminal commands on my VM, verified all outputs against the repository, and I am responsible for explaining every claim in this project.
