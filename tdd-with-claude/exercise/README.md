---
tags:
  - ai-generated
---
# Exercise: a room heater, test first

The controller in `controller.py` is a stub. Build it test first from [SPEC.md](SPEC.md).

| File | What |
|---|---|
| `SPEC.md` | What the controller must do |
| `controller.py` | The controller, a stub for now |
| `heater.py` | Room model and the two scenarios. `python heater.py` plots them. |
| `test_heater.py` | One smoke test to start from |

## Setup

**Codespaces.** On GitHub, click **Code → Codespaces → New with options** and pick
**TDD with Claude**. Then `cd tdd-with-claude/exercise`.

**Locally with uv** (macOS, Linux, Windows). Install [uv](https://docs.astral.sh/uv/), then:

```bash
cd tdd-with-claude/exercise
uv run --with-requirements requirements.txt pytest -v
uv run --with-requirements requirements.txt python heater.py
```

**Locally with pip.** You need Python 3.10 or newer.

| | macOS, Linux | Windows (PowerShell) |
|---|---|---|
| Create venv | `python3 -m venv .venv` | `py -m venv .venv` |
| Activate | `source .venv/bin/activate` | `.venv\Scripts\Activate.ps1` |
| Install | `pip install -r requirements.txt` | same |
| Test | `pytest -v` | same |
| Plot | `python heater.py` | same |

If PowerShell refuses to activate the venv, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once.

`python heater.py` saves `heater.png`. Open it in any image viewer.

## With Claude Code

Copy the [tdd skill](../skills/tdd/SKILL.md) to your skills folder:

| macOS, Linux | Windows (PowerShell) |
|---|---|
| `cp -r ../skills/tdd ~/.claude/skills/` | `Copy-Item -Recurse ..\skills\tdd ~\.claude\skills\` |

Then start `claude` in this folder and say *"Let's build the controller test-first from
SPEC.md."*
