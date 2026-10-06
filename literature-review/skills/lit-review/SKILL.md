---
name: lit-review
description: Runs literature review rounds with OpenAlex, a reading log and one review file per round, kept in git. No reference manager needed. Use when planning a review, searching or snowballing papers, adding a paper, writing reading log entries or review files, or checking a citation.
tags:
  - ai-generated
---
# Literature review

## Requires

If one is missing, say so and stop.

- A git repo with `reading-log.md`, a `reviews/` folder, and `pdfs/` in `.gitignore`. Offer to
  create them when they are missing.
- Optional: an OpenAlex key at `~/.config/openalex/api-key`. Without it the daily budget is
  10 times smaller.

Paths: `reading-log.md`, `reviews/` and `pdfs/` are in the working folder. `scripts/` and
`references/` are in this skill's folder.

## Adding a paper

The same rule for a single paper and for papers found in a round.

1. Check for a duplicate: grep the DOI in the reading log. If the paper is already there,
   say so and stop.
2. Check the abstract: `python3 <skill folder>/scripts/openalex_abstract.py <DOI>`. Exit code
   1 means OpenAlex has none. A paper without an abstract is a judgment call, not an
   automatic skip. Weigh how often it is cited, whether papers in the round cite it, and its
   age: classics and very new papers often lack one. If added, its Source is `secondary`.
   Either way, say why, and in a round note it in the Search log.
3. Give it a citekey: the first author's last name in lowercase plus the year, like
   `smith2020`. Add `a`, `b` if the log already has it.
4. Write the reading log entry. In a round it goes under the round's heading. A single paper
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

1. **Check what is known.** Grep the reading log, so the plan builds on what is there.
2. **Plan.** Agree on the review question, split into a few sub-questions, plus search terms,
   venues, years and what counts as in or out. If this is the first round, propose the tier
   definitions in the same question. Do not search before the user says go. After the go,
   start the review file with Questions and Plan, in the format in
   [references/formats.md](references/formats.md).
3. **Search and add.** Use the tools below. Write each search into the review file's Search
   log: query, source, filter, hits, papers added. Add papers as in "Adding a paper".
4. **Request full texts.** List the papers that must be read in full to be judged reliably:
   likely core papers, and papers whose numbers, setup or model the review depends on. First
   fetch what is open access: OpenAlex `best_oa_location`, Europe PMC, arXiv. Then give the
   rest to the user, each with its DOI link and the reason. Ask them to download those into
   `pdfs/` as `<citekey>.pdf`, and wait.
5. **Write the reading log.** A round heading with a link to the review file, then one entry
   per paper. Then fill Papers found in the review file. Formats are in
   [references/formats.md](references/formats.md).
6. **Pick one to three must-reads** for the user, in reading order: foundations first, then
   details. Write them into the review file. Each must be on the step 4 list, so its entry
   was written from the full text.
7. **Write the synthesis** in the review file. Check each key claim against the paper text.
   Then commit the reading log and the review file.

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
