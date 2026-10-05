---
name: lit-review
description: Runs literature review rounds with Zotero, OpenAlex, a reading log and one review file per round, kept in git. Use when planning a review, searching or snowballing papers, adding papers to Zotero, writing reading log entries or review files, or checking a citation.
tags:
  - ai-generated
---
# Literature review

## Requires

Check these before the first round. If one is missing, say so and stop.

- **Zotero MCP**, [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp), installed as
  `zotero-mcp-server[semantic]`, registered under the name `zotero`, in web API mode.
  Check with `zotero:zotero_write_capabilities`.
- **Better BibTeX** in Zotero, so every item has a citekey. Check that one item's
  `zotero:zotero_get_item_metadata` with `format="json"` shows a `citationKey`.
- **OpenAlex key** at `~/.config/openalex/api-key`. Optional. Without it the daily budget is
  10 times smaller.
- **A reading log** `reading-log.md` in a git repo, and a `reviews/` folder for review files.

Paths: `reading-log.md` and `reviews/` are in the working folder. `scripts/` and
`references/` are in this skill's folder.

## Quick tasks

Adding one paper or checking a citation needs no round.

1. Check for a duplicate: grep the reading log, then search Zotero by DOI.
2. Check the abstract with `scripts/openalex_abstract.py`. No abstract anywhere means do not
   add, and say why.
3. Ask which collection it belongs in, then add it as described in
   [references/zotero-mcp.md](references/zotero-mcp.md).

## Workflow

One round at a time. Copy this checklist into the chat and tick it off. The user is asked
twice, at step 1 and step 4. Do not continue past either before the user answers.

```
Round progress:
- [ ] 1. Plan agreed
- [ ] 2. Known papers checked
- [ ] 3. Searched and added
- [ ] 4. Full texts requested and downloaded
- [ ] 5. Reading log written
- [ ] 6. Must-reads picked
- [ ] 7. Synthesis written
```

1. **Plan.** Agree on the review question, split into two or three sub-questions, plus search
   terms, venues, years and what counts as in or out. If the reading log is new, propose the
   tier definitions in the same question. Start the review file with Questions and Plan, in
   the format in [references/formats.md](references/formats.md). Do not search before the
   user says go. After the go, create the round's Zotero collection with
   `zotero:zotero_create_collection`, named after the round.
2. **Check what is known.** Grep the reading log first, then search Zotero.
3. **Search and add.** Use the tools below. Write each search into the review file's Search
   log: query, source, filter, hits, papers added.
   - A paper needs at least an abstract to be added. Before adding, run
     `python3 <skill folder>/scripts/openalex_abstract.py <DOI>`. Exit code 1 means OpenAlex
     has none. If no other source has one either, do not add the paper. List it as skipped,
     with the reason.
   - After adding, if the Zotero item has no abstract, write the script output into it with
     `zotero:zotero_update_item`.
   - Attach the open access PDF when one exists.
4. **Request full texts.** List the papers that must be read in full to be judged reliably:
   likely core papers, and papers whose numbers, setup or model the review depends on. Give
   each with its DOI link and the reason. Ask the user to download them, for example with
   the Zotero Connector, and wait.
5. **Write the reading log.** A round heading with a link to the review file, then one entry
   per paper. Then fill Papers found in the review file. Formats are in
   [references/formats.md](references/formats.md).
6. **Pick one to three must-reads** for the user, in reading order: foundations first, then
   details. Write them into the review file. Each must be on the step 4 list, so its entry
   was written from the full text.
7. **Write the synthesis** in the review file. Check each key claim against the paper text
   through the MCP. Then commit the reading log and the review file.

If nothing good was found, say so plainly. An empty result is a valid result. Never pad the
list to look productive.

## Tools

- **OpenAlex** first. Search with `api.openalex.org/works?search=...`, look up a DOI with
  `api.openalex.org/works/doi:<doi>`, find citing papers with `works?filter=cites:<id>`.
  Send the key in the header, `-H "Authorization: Bearer $(cat ~/.config/openalex/api-key)"`.
  Never print it or put it in a URL.
- **Zotero MCP** for finding, reading and adding papers. Read
  [references/zotero-mcp.md](references/zotero-mcp.md) before the first call.
- **Google Scholar** as a second check for venues OpenAlex misses. It has no API and blocks
  scripts. Use it only through the browser. At any CAPTCHA, stop and hand the user the link.
