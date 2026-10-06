---
name: lit-review-zotero
description: Runs literature review rounds with OpenAlex, a Zotero library through the Zotero MCP, a reading log and one review file per round, kept in git. Use when planning a review, searching or snowballing papers, adding papers to Zotero, finding papers by citekey or DOI, reading PDFs and highlights, writing reading log entries or review files, or checking a citation.
tags:
  - ai-generated
---
# Literature review with Zotero

Zotero additions to the plain `lit-review` skill are marked **Zotero:**.

## Requires

If a Zotero check fails, say so and stop.

- `reading-log.md` and a `reviews/` folder in the working folder. Create them if they are
  missing.
- If the folder is not backed up, neither a git repo nor a synced folder like Google Drive
  or Dropbox, say so and recommend setting that up. Then continue.
- Optional: an OpenAlex key at `~/.config/openalex/api-key`. Without it the daily budget is
  10 times smaller.
- **Zotero:** the Zotero MCP, registered as `zotero`, so its tools are named `mcp__zotero__*`.
  Check with `mcp__zotero__zotero_write_capabilities`.
- **Zotero:** Better BibTeX. Check that an item added more than a day ago shows a
  `citationKey` in `mcp__zotero__zotero_get_item_metadata` with `format="json"`.

Zotero tools and rules are in [references/zotero.md](references/zotero.md). Read it before the
first Zotero call.

Paths: `reading-log.md` and `reviews/` are in the working folder. `scripts/` and
`references/` are in this skill's folder.

## Adding a paper

The same rule for a single paper and for papers found in a round.

1. Check for a duplicate: grep the DOI in the reading log. If the paper is already there,
   say so and stop. **Zotero:** also search the library by DOI. If it is there but not in the
   log, say which collections it is in and offer to write the entry.
2. Check the abstract: `python3 <skill folder>/scripts/openalex_abstract.py <DOI>`. Exit code
   1 means OpenAlex has none. A paper without an abstract is only added if it seems
   promising, for example a well-cited classic or a paper the round's papers cite. It then
   goes on the list of papers the user downloads, and the Search log says why.
3. **Zotero:** add it with `if_exists="file"` into the round's collection, or ask which
   collection for a single paper. arXiv papers go in by arXiv URL. If the item has no
   abstract, write it in with `mcp__zotero__zotero_update_item`.
4. Give it a citekey: its `citationKey` from Better BibTeX. Right after an API add it is
   empty until Zotero desktop syncs. Meanwhile use the first author's last name in lowercase
   plus the year, like `smith2020`, and check after the sync that they match.
5. Write the reading log entry, with the Zotero key. In a round it goes under the round's heading. A single paper
   goes under `## Single papers` with the date it was added.

## Workflow

One round at a time. Copy this checklist into the chat and tick it off. The user is asked
twice, at step 2 and step 4. Do not continue past either before the user answers.

```
Round progress:
- [ ] 1. Known papers checked
- [ ] 2. Plan agreed
- [ ] 3. Searched and added
- [ ] 4. Full texts requested and downloaded
- [ ] 5. Reading log written
- [ ] 6. Must-reads picked
- [ ] 7. Synthesis written
```

1. **Check what is known.** Grep the reading log. **Zotero:** then search the library. The
   plan builds on what is there.
2. **Plan.** Agree on the review question, split into a few sub-questions, plus search terms,
   venues, years and what counts as in or out. Do not search before the user says go. After the go,
   start the review file with Questions and Plan, in the format in
   [references/formats.md](references/formats.md). **Zotero:** create the round's collection,
   named after the round.
3. **Search and add.** Use the tools below. Write each search into the review file's Search
   log: query, source, filter, hits, papers added. Add papers as in "Adding a paper".
4. **Request full texts.** List the papers that must be read in full to be judged reliably:
   likely core papers, papers whose numbers, setup or model the review depends on, and
   promising papers without an abstract. First
   fetch what is open access: OpenAlex `best_oa_location`, Europe PMC, arXiv. Then give the
   rest to the user, each with its DOI link and the reason. **Zotero:** fetched PDFs are
   attached with `mcp__zotero__zotero_attach_file`. The user saves the rest with the Zotero
   Connector. Wait until they say done.
5. **Write the reading log.** A round heading with a link to the review file, then one entry
   per paper. Then fill Papers found in the review file, with each paper's relevance for
   this review. Formats are in
   [references/formats.md](references/formats.md).
6. **Pick one to three must-reads** for the user, in reading order: foundations first, then
   details. Write them into the review file. Each must be on the step 4 list, so its entry
   was written from the full text.
7. **Write the synthesis** in the review file. Check each key claim against the paper text.
   Then commit the reading log and the review file. **Zotero:** also commit the `.bib` file if
   Better BibTeX auto-exports one into the repo, then run
   `mcp__zotero__zotero_update_search_database`.

If nothing good was found, say so plainly. An empty result is a valid result. Never pad the
list to look productive.

## Tools

- **OpenAlex** first. Search with `api.openalex.org/works?search=...`, look up a DOI with
  `api.openalex.org/works/doi:<doi>`, find citing papers with `works?filter=cites:<id>`.
  The open access PDF, when there is one, is in `best_oa_location.pdf_url`.
  Use plain `search=` with a `publication_year` filter. Boolean syntax inside
  `title_and_abstract.search` is not a conjunction and returns unrelated papers. Send the key in
  the header, `-H "Authorization: Bearer $(cat ~/.config/openalex/api-key)"`. Never print it
  or put it in a URL.
- **Google Scholar** as a second check for venues OpenAlex misses. It has no API and blocks
  scripts. Use it only through the browser. At any CAPTCHA, stop and hand the user the link.
