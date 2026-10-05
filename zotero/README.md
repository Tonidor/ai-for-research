---
tags:
  - ai-generated
---
# Zotero with Claude

Gives Claude your Zotero library through the Zotero MCP: search by DOI, citekey or topic,
read PDFs and highlights, and add papers without creating duplicates. The `lit-review` skill
uses it when it is installed.

Needs Claude Code on the command line, see [literature-review](../literature-review/), setup
step 1. Steps marked **macOS** or **Linux** differ by system.

## 1. Zotero MCP

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

## 2. Better BibTeX

Gives every paper a stable citekey like `smith2020` and keeps a `.bib` file for LaTeX.

1. Install the `.xpi` from the [releases page](https://github.com/retorquere/zotero-better-bibtex/releases)
   via Zotero, Tools, Plugins, gear icon, Install Plugin From File.
2. Open the settings. **macOS:** Zotero, Settings. **Linux:** Edit, Settings.
3. Better BibTeX, Citation keys: formula `auth.lower + year`.
4. Better BibTeX, Export, Fields: omit `file`, so no local paths end up in git.
5. Right-click the library, Export Library, Better BibTeX, tick "Keep updated". Save it into
   your review folder.

## 3. The skill

Copy the `zotero/` skill folder into your working folder:

```bash
mkdir -p .claude/skills && cp -R <path to this repo>/zotero/zotero .claude/skills/
```

## Rules worth knowing

- Adding always uses `if_exists="file"`. The default creates duplicates.
- Semantic search only sees titles for items without an abstract.
- Claude never writes notes into Zotero and asks before deleting.
