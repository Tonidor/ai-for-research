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
- **Zotero** is optional. With the `zotero` skill, papers and PDFs also go into your Zotero
  library. See [Optional: Zotero](#optional-zotero).

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

### 3. The lit-review skill

Copy the `lit-review/` folder from this repo into your review folder:

```bash
mkdir -p .claude/skills && cp -R <path to this repo>/literature-review/lit-review .claude/skills/
```

Then create an empty `reading-log.md` and a `reviews/` folder next to it, add `pdfs/` to
`.gitignore`, and commit. Or ask Claude to do it.

For Zotero, continue with [Optional: Zotero](#optional-zotero).

## Optional: Zotero

Gives Claude your Zotero library: search by DOI, citekey or topic, read PDFs and highlights,
and add papers without creating duplicates. `lit-review` uses it automatically when the
`zotero` skill is installed.

### 4. Zotero MCP

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

### 5. Better BibTeX

Gives every paper a stable citekey like `smith2020` and keeps a `.bib` file for LaTeX.

1. Install the `.xpi` from the [releases page](https://github.com/retorquere/zotero-better-bibtex/releases)
   via Zotero, Tools, Plugins, gear icon, Install Plugin From File.
2. Open the settings. **macOS:** Zotero, Settings. **Linux:** Edit, Settings.
3. Better BibTeX, Citation keys: formula `auth.lower + year`.
4. Better BibTeX, Export, Fields: omit `file`, so no local paths end up in git.
5. Right-click the library, Export Library, Better BibTeX, tick "Keep updated". Save it into
   your review folder.

### 6. The zotero skill

Copy the `zotero/` skill folder next to `lit-review/`:

```bash
mkdir -p .claude/skills && cp -R <path to this repo>/literature-review/zotero .claude/skills/
```

### Rules worth knowing

- Adding always uses `if_exists="file"`. The default creates duplicates.
- Semantic search only sees titles for items without an abstract.
- Claude never writes notes into Zotero and asks before deleting.

## Use

Start a session in your review folder and type `/lit-review`, then your question. Claude
agrees on a plan with you before searching, asks you to download the papers that need a full
read, and writes the reading log and the review file. To add one paper, give it the DOI.

With the `zotero` skill installed as well, papers also go into your Zotero library.
Nothing changes in how you use `/lit-review`.

## Tutorial, 10 minutes

Live, everyone on their own laptop. Participants need only Claude Code and the `lit-review`
skill. The last step is a demo by the presenter, who has the `zotero` skill set up.

| Min | Show | Participants do | Point |
|---|---|---|---|
| 2 | Ask Claude for 5 papers on a topic, with DOIs, no tools | Check each DOI at `api.openalex.org/works/doi:<doi>` | Some do not exist. Never trust a reference from memory |
| 2 | Same question, Claude searches OpenAlex | Pick one result, ask who cites it | Real papers, and snowballing in one call |
| 3 | `/lit-review` and the DOI of that paper | Add it, read the entry, set the tier yourself | The abstract is checked. The log holds the judgment, Claude only drafts it |
| 3 | Demo with Zotero: add a paper that is already in the library but not in the log | Watch | Found in Zotero by DOI, nothing added twice. Then ask for its highlights |

Want the Zotero part as well? Follow [Optional: Zotero](#optional-zotero) afterwards.
