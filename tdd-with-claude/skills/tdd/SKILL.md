---
name: tdd
description: Test-driven development with the user. Agrees on a spec, proposes tests, then works red, green, refactor one test at a time. Use when the user wants to write or change code test-first, or asks for TDD.
tags:
  - ai-generated
---
# TDD

## Requires Claude Code

This skill needs a shell to run tests. If you cannot run shell commands, tell the user to
open the project in Claude Code and stop.

## 1. Branch

If the project uses git, propose a branch name that fits the task, like
`feat/anti-windup`, and ask whether to create it.

## 2. Spec

Ask the user for a spec. If there is none, develop one together: what the code must do,
under which conditions, with measurable criteria. Keep it short. Get the user's OK before
moving on.

## 3. Tests

Show a table that maps each requirement to the tests that cover it. Below it, suggest
general checks where they apply: edge cases, invalid input, limits, error handling,
security. Mark these as beyond the spec. Ask the user to confirm the list once.

## 4. Red, green, refactor

Work through the whole list without stopping. Do not ask between tests.

For each test:

1. **Red.** Write the test. Run it with the project's test runner. Confirm it fails for
   the right reason. If it passes right away, say so and move on.
2. **Green.** Write the minimum code that makes it pass. Nothing a later test asks for.
   Run all tests.
3. **Refactor.** Only if it helps. All tests stay green.

After each step, print a one-line status: test name, red or green, what changed.

Do not change a test once it is written. If a test seems wrong, stop, explain why and
propose a change. Apply it only after the user confirms, then continue.

When all tests are green, show a summary table: test, requirement, status.

## 5. Commit

If the project uses git, ask whether to commit and push. If yes, use a conventional
commit message.
