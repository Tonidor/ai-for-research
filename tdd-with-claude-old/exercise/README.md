---
tags:
  - ai-generated
---
# Exercise: a room heater, test first

A PI controller heats a room to 21 °C. It runs, and the step response looks fine. Is it correct?
Write tests from [SPEC.md](SPEC.md) and find out.

| File | What |
|---|---|
| `room.py` | First-order thermal model of the room |
| `controller.py` | The PI controller |
| `simulate.py` | Closed loop: room plus controller |
| `plot.py` | Saves the step response to `step_response.png` |
| `SPEC.md` | What the controller must do |
| `tests/` | One smoke test to start from |

## Setup

**Codespaces.** On GitHub, click **Code → Codespaces → New with options** and pick
**TDD with Claude**. Then `cd tdd-with-claude/exercise`.

**Locally.** You need Python 3.10 or newer.

```bash
cd tdd-with-claude/exercise
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Check that it works:

```bash
pytest
python plot.py
```

## With Claude Code

1. Copy the skill: `cp -r ../skills/tdd ~/.claude/skills/`
2. Start `claude` in this folder and say: *"Let's do TDD on the controller against SPEC.md."*
3. Claude asks for your test ideas first. Give a few, then let it add the ones you missed.
4. Claude runs `pytest` and `git` itself. You review each red and each green.

## With claude.ai

1. Zip the `../skills/tdd` folder and upload it under **Settings → Capabilities → Skills**.
2. Start a chat. Attach `SPEC.md`, `room.py`, `controller.py`, `simulate.py` and
   `tests/test_smoke.py`. Say: *"Let's do TDD on the controller against SPEC.md."*
3. Claude gives you the code and the exact commands. Run them in your terminal and paste the
   output back.

## Spoiler

<details>
<summary>What is wrong with the controller?</summary>

It has no anti-windup. While the heater is stuck at 100 %, the integrator keeps growing. When
the window closes, the stored integral drives the room far above the setpoint. Requirement 7
catches it. The nominal step never saturates, so requirements 1 to 6 pass.

</details>
