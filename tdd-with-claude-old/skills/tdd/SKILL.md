---
name: tdd
description: Guides test-driven development together with the user. Red, green, refactor, one test at a time, from a spec. Use when the user wants to do TDD, write tests from a spec, or fix code test-first.
tags:
  - ai-generated
---
# TDD with the user

The user stays in the loop. Do not write all tests alone. Do not skip the red step.

## Where you run

- **Claude Code:** run `pytest` and `git` yourself. Show the user the relevant output.
- **claude.ai or any chat without a shell:** you cannot run anything. Give the exact command
  in a code block, ask the user to run it and paste the output. Wait for the output before
  you go on. Give code as complete files, so the user can copy them as they are.

## 1. Branch

Check the current branch with `git branch --show-current`. If it is `main` or `master`,
create a feature branch: `git switch -c <type>/<short-name>`, for example
`git switch -c fix/anti-windup`. Never commit to main.

## 2. Read the spec

Read `SPEC.md` and the code it names. Summarize the requirements in one short list. Ask the
user if anything is unclear before you go on.

## 3. Brainstorm tests with the user

1. Ask the user first: "Which tests would you write?" Wait for the answer.
2. Map their ideas to the requirements.
3. Then name what is missing: requirements with no test, edge cases, saturation, limits.
4. Agree on one list, ordered from simplest to hardest. Keep it short.

## 4. Red, green, refactor

For each test on the list:

1. **Red.** Write one test. Run `pytest`. Confirm it fails for the right reason. If it passes
   right away, say so. The code already meets that requirement, which is fine. Move on.
2. **Green.** Write the smallest change to the code that makes it pass. Run all tests.
3. **Refactor.** Clean up only if it helps. Run all tests again. They must stay green.

Show the user each red and each green. Never change a test to make it pass unless the user
agrees the test was wrong.

## 5. Commit and push

When all tests are green:

1. Show `git status` and `git diff --stat`.
2. Commit with a conventional commit message, for example
   `fix(controller): add anti-windup to the PI integrator`. Use `test:` for test-only commits.
3. Push: `git push -u origin <branch>`.
