---
tags:
  - ai-generated
---
# Literature review with Claude

Claude searches papers and keeps a reading log and one review file per round in git. You
make the judgments. Never trust a reference Claude writes from memory. Every paper comes from
a search tool or a library.

The tutorial is [tutorial.html](tutorial.html). Open it in a browser.

## Choose a version

| Skill | Papers live in | Needs |
|---|---|---|
| `lit-review` | the reading log and a `pdfs/` folder | Claude Code |
| `lit-review-zotero` | your Zotero library, plus the reading log | Claude Code, the Zotero MCP, Better BibTeX |

Both run the same review rounds. Install one of them, not both. The skills are in
[skills/](skills/).

## Setup for lit-review

No setup beyond getting the skill. It works in any Claude Code: the desktop app, the command
line or an IDE.

1. Get this repo, with `git clone https://github.com/Tonidor/ai-for-research.git`, or download
   it as a ZIP from GitHub. Later, `git pull` gets updates.
2. Copy the skill into your review folder:
   ```bash
   mkdir -p .claude/skills && cp -R <path to this repo>/literature-review/skills/lit-review .claude/skills/
   ```
3. Start Claude in that folder and type `/lit-review`. The skill tells you if anything else is
   missing.

## Setup for lit-review-zotero

Gives Claude your Zotero library: search by DOI, citekey or topic, read PDFs and highlights,
and add papers without creating duplicates.

Tested on macOS with the Claude desktop app. Steps marked **macOS** or **Linux** differ by
system. Run every command in a real terminal, not in Claude's `!` shell.

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

### 3. Zotero MCP

1. Install `uv`, the Python tool installer, if `uv --version` fails.
   - **macOS:** `brew install uv`
   - **Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Find your library ID.
   - Group library: the number in the group's URL on zotero.org, `zotero.org/groups/<ID>/...`.
   - Personal library: "Your userID" on [zotero.org/settings/keys](https://www.zotero.org/settings/keys).
3. Create an API key at [zotero.org/settings/keys](https://www.zotero.org/settings/keys).
   Give it access only to the library you review in. Read/Write lets Claude add papers.
4. Save the key:
   ```bash
   mkdir -p ~/.config/zotero && printf 'Key: ' && stty -echo && read k && stty echo && echo && printf '%s' "$k" > ~/.config/zotero/api-key && chmod 600 ~/.config/zotero/api-key
   ```
5. Install the server with semantic search:
   ```bash
   uv tool install --python 3.12 "zotero-mcp-server[semantic]"
   ```
6. Register it, from the folder you will work in. Use `group` or `user` as the type.
   The name `zotero` must come first.
   ```bash
   claude mcp add zotero --scope local -e ZOTERO_LIBRARY_ID=<ID> -e ZOTERO_LIBRARY_TYPE=group -- sh -c 'ZOTERO_API_KEY="$(cat ~/.config/zotero/api-key)" exec ~/.local/bin/zotero-mcp'
   ```
7. Check it: `claude mcp get zotero` should say Connected.
8. Build the search index once. Run it again after adding papers.
   ```bash
   ZOTERO_API_KEY="$(cat ~/.config/zotero/api-key)" ZOTERO_LIBRARY_ID=<ID> ZOTERO_LIBRARY_TYPE=group zotero-mcp update-db
   ```

### 4. Better BibTeX

Gives every paper a stable citekey like `smith2020` and keeps a `.bib` file for LaTeX.

1. Install the `.xpi` from the [releases page](https://github.com/retorquere/zotero-better-bibtex/releases)
   via Zotero, Tools, Plugins, gear icon, Install Plugin From File.
2. Open the settings. **macOS:** Zotero, Settings. **Linux:** Edit, Settings.
3. Better BibTeX, Citation keys: formula `auth.lower + year`.
4. Better BibTeX, Export, Fields: omit `file`, so no local paths end up in git.
5. Right-click the library, Export Library, Better BibTeX, tick "Keep updated". Save it into
   your review folder. Required: the skill checks for this `.bib` before the first round.

### 5. The skill

Copy the skill into your review folder:

```bash
mkdir -p .claude/skills && cp -R <path to this repo>/literature-review/skills/lit-review-zotero .claude/skills/
```

Then create an empty `reading-log.md` and a `reviews/` folder next to it, and commit. Or ask
Claude to do it.

## Use

Start Claude in the folder that holds `.claude/skills/`, your review folder. Started anywhere
else, the skill is not found. Type `/lit-review` or `/lit-review-zotero`, then your question.
Claude agrees on a plan with you before searching, asks you to download the papers that need
a full read, and writes the reading log and the review file. To add one paper, give it the DOI.

## Maintaining the two skills

`lit-review` is the minimal version. `lit-review-zotero` adds Zotero, the OpenAlex key and
more detail, and marks its Zotero parts **Zotero:**. A change to the review workflow itself
goes into both.
