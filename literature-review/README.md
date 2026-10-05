---
tags:
  - ai-generated
---
# Literature review with Claude

Claude searches papers and keeps a reading log and one review file per round in git. You
make the judgments.

- **OpenAlex** finds papers, checks DOIs and follows citations. No install needed.
- **The `lit-review` skill** holds the workflow and the formats.
- **Git** holds your reading log and review files.
- **Zotero** is optional. With the [zotero](../zotero/) skill, papers and PDFs also go into
  your Zotero library.

Never trust a reference Claude writes from memory. Every paper comes from a search tool or
from Zotero.

## Setup

Tested on macOS with the Claude desktop app. Steps marked **macOS** or **Linux** differ by
system, everything else is the same on both. Run every command in a real terminal, not in
Claude's `!` shell.

### 1. Claude Code on the command line

The desktop app does not install the `claude` command.

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Then put `~/.local/bin` on the PATH.

- **macOS** (zsh is the default shell):
  ```bash
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
  ```
- **Linux** (bash is the usual default):
  ```bash
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
  ```

Then log in once: run `claude` and type `/login`. The desktop app's login does not carry over.

### 2. OpenAlex key (optional)

Free. Without it the daily budget is 10 times smaller.

1. Make an account and copy the key from [openalex.org/settings/api](https://openalex.org/settings/api).
2. Save it without showing it on screen:
   ```bash
   mkdir -p ~/.config/openalex && printf 'Key: ' && stty -echo && read k && stty echo && echo && printf '%s' "$k" > ~/.config/openalex/api-key && chmod 600 ~/.config/openalex/api-key
   ```

Never paste a key into the chat.

### 3. The skill

Copy the `lit-review/` folder from this repo into your review folder:

```bash
mkdir -p .claude/skills && cp -R <path to this repo>/literature-review/lit-review .claude/skills/
```

Then create an empty `reading-log.md` and a `reviews/` folder next to it, add `pdfs/` to
`.gitignore`, and commit. Or ask Claude to do it.

For Zotero, also set up the [zotero](../zotero/) skill.

## Use

Start a session in your review folder and type `/lit-review`, then your question. Claude
agrees on a plan with you before searching, asks you to download the papers that need a full
read, and writes the reading log and the review file. To add one paper, give it the DOI.

With the [zotero](../zotero/) skill installed as well, papers also go into your Zotero library.
Nothing changes in how you use `/lit-review`.

## Tutorial, 10 minutes

Live, everyone on their own laptop. Participants need only Claude Code and the `lit-review`
skill. The last step is a demo by the presenter, who has the `zotero` skill set up.

| Min | Show | Participants do | Point |
|---|---|---|---|
| 2 | Ask Claude for 5 papers on a topic, with DOIs, no tools | Check each DOI at `api.openalex.org/works/doi:<doi>` | Some do not exist. Never trust a reference from memory |
| 2 | Same question, Claude searches OpenAlex | Pick one result, ask who cites it | Real papers, and snowballing in one call |
| 3 | `/lit-review` and the DOI of that paper | Add it, read the entry, set the tier yourself | The abstract is checked. The log holds the judgment, Claude only drafts it |
| 3 | Demo: the same DOI again, now with Zotero | Watch | It is found in Zotero by DOI and not added twice. Highlights and PDFs are readable too |

Want the Zotero part as well? Follow the [zotero](../zotero/) setup afterwards.
