# Student 3 Individual Reflection (Moayad Alahmadi)

## Difficulty

I joined the work on day 3, with the repository already started and no experience of GitHub Actions. My first pipeline run failed, and later I found that the image saved by a pull-request run was named after a commit that does not exist in our history.

## How I responded

- I started from what the brief asks of the CI lead: tests, a static check, and a versioned artifact that is only built when both pass. I put the tests and the workflow in one pull request (PR #1) so a reviewer could see them together.
- I kept the failed run (flake8 `W391`) instead of hiding it, fixed it in a separate commit, and used the failed and passing runs as the required evidence.
- For the naming problem I compared the artifact name (`dc1fe30…`) with my commit (`7187870`) and learned that on a pull request `github.sha` is GitHub's temporary merge commit. PR #6 uses the PR head commit instead, and run #13 confirmed the fix (artifact `devops-info-sha-f927fc2`, matching commit `f927fc2`).

## Next improvement

Release tags are not protected: the `v1.0.0` tag was deleted and re-created on a different commit, which broke the link between the tag and the deployed image. Next I would add a GitHub tag ruleset so that `v*` tags cannot be deleted or moved, and add a pipeline step that fails if a release already exists for that tag.

## Assistance disclosure

I used an AI assistant (Claude) to help draft the tests, the workflow and these records. I ran the tests and checks, reviewed every change, and I am responsible for explaining them.
