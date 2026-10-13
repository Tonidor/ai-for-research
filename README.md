# AI for research

Tutorials and skills for working with Claude in research. One folder per topic. Copy what you
need into your own projects.

| Folder | Topic | What it is | Added |
|---|---|---|---|
| [`git-with-claude/`](git-with-claude/) | Git | Why git makes working with Claude safe, and how to set up `gh` | 2026-09-22 |
| [`literature-review/`](literature-review/) | Skills | Literature reviews with OpenAlex and a reading log, in two versions: `lit-review`, and `lit-review-zotero` with Zotero | 2026-10-05 |
| [`mock-exam/`](mock-exam/) | Subagents | An example of how to use subagents: student agents, each playing a persona, sit a new exam in parallel; blind grader agents mark it; analyst agents propose edits to the exam. | 2026-10-12 |
| [`simplified-research-english/`](simplified-research-english/) | Skills | A writing skill based on ASD-STE100 Simplified Technical English, with rules and a dictionary that you can change to fit your own style | 2026-10-13 |

`mock-exam/` is its own Claude Code project. Open Claude Code inside the folder (`cd mock-exam && claude`) so that its agents, workflows and hooks load.

To get updates, run `git pull` and copy the changed files again.
