---
tags:
  - ai-generated
---
# Simplified Research English

A Claude Code skill that writes and checks research text in a controlled style. The style comes
from ASD-STE100 Simplified Technical English, the standard for aircraft maintenance manuals.
Andrej Karpathy [suggested](https://x.com/karpathy/status/2105819303471976479) that you ask an
LLM for ASD-STE100 to make its output easier to read.

## Why a skill and not a prompt

A one-line prompt already does most of the work: “Rewrite this text in ASD-STE100.” But then the
model uses its own idea of the standard, and the result changes from one session to the next.

A skill puts the rules and the vocabulary in files that you control. Thus, you can change them to
fit your own style:

- **Vocabulary.** The dictionary fixes the words of your field: one name for each concept, the
  words to avoid, and the default symbols. ASD-STE100 has a list of approved words for aircraft
  maintenance, not for your research.
- **Rules.** You can keep, change, or remove each rule, and you can add your own. This copy adds
  rules for research claims, for example evidence words (“show”, “suggest”, “expect”) that tell
  how strong a claim is.
- **Checks.** A script checks the rules that a model does not apply reliably: sentence length,
  semicolons, passive voice, and the words of the dictionary.
- **The same result each time.** Each session reads the same files.

## What is in the skill

The skill is in [skills/simplified-research-english/](skills/simplified-research-english/).

| File | What it is |
|---|---|
| `SKILL.md` | The main instructions: seven steps, from the type of text to the final check |
| `references/writing-rules.md` | The 53 rules and 4 recommendations of ASD-STE100 with research examples, and 8 rules for research claims |
| `references/dictionary.md` | Evidence words, connecting words, words to avoid, and the technical names, verbs, and symbols of one field |
| `examples/before-after.md` | Research text before and after the rewrite |
| `scripts/check.py` | The check tool for Markdown, LaTeX, and HTML files |
| `NOTICE.md` | Sources and licenses |

## Setup

1. Get this repo, with `git clone https://github.com/Tonidor/ai-for-research.git`, or download
   it as a ZIP from GitHub. Later, `git pull` gets updates.
2. Copy the skill into your skills folder:
   ```bash
   mkdir -p ~/.claude/skills && cp -R <path to this repo>/simplified-research-english/skills/simplified-research-english ~/.claude/skills/
   ```
   For one project only, copy it into the `.claude/skills/` folder of that project.
3. In Claude Code, type `/simplified-research-english`, or ask Claude to rewrite or check a text
   with the skill.

You can also run the check tool without Claude:

```bash
python3 ~/.claude/skills/simplified-research-english/scripts/check.py --mode descriptive paper.tex
```

## Make it yours

This copy is Kai's version. Sections 4 to 7 of its dictionary have example entries from control and
game theory. Before you use the skill:
- Replace `Kai` with your name.
- Give Claude some materials to adapt the dictionary and rules to make the skill yours. For example, ask Claude to scan your Zotero library.
- And then iterate and adapt.

## Other repos

- [0xpili/simplified-technical-english](https://github.com/0xpili/simplified-technical-english):
  an Agent Skill with the 53 rules of ASD-STE100, the approved word list, and a check script. This
  skill started from it.
- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill): applies the STE rules
  to text that agents read, for example prompts and tool descriptions, with a linter.
- [ChangWenC/understanding-ladder](https://github.com/ChangWenC/understanding-ladder): Karpathy's
  four formats as skills. It selects text, a diagram, an interactive page, or a video storyboard.
- [ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style): four
  skills for clear writing, Excalidraw diagrams, interactive HTML, and narrated videos.
- [asd-ste100.org](https://www.asd-ste100.org/): the official site of the standard. You can
  request a free copy of Issue 9 (January 2025) on its
  [downloads page](https://www.asd-ste100.org/STE_downloads.html).

## License

The rules in sections 1 to 9 and parts of the check tool come from 0xpili/simplified-technical-english
(MIT license). ASD owns ASD-STE100, and this skill does not contain the specification or the STE
dictionary. Refer to [NOTICE.md](skills/simplified-research-english/NOTICE.md).
