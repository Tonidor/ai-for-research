---
name: lit-review
description: Runs literature review rounds with OpenAlex, a reading log and one review file per round. No reference manager needed. Use when planning a review, searching or snowballing papers, adding a paper, writing reading log entries or review files, or checking a citation.
tags:
  - ai-generated
---
# Literature review

## Before the first round

- The working folder needs `reading-log.md`, a `reviews/` folder and a `pdfs/` folder.
  Create them if they are missing.
- The abstract script needs `python3`. If `python3 --version` fails, tell the user how to get
  it. **macOS:** `xcode-select --install`. **Linux:** the package manager, for example
  `sudo apt install python3`. Nothing else needs installing.
- If the folder is not backed up, neither a git repo nor a synced folder like Google Drive
  or Dropbox, say so and recommend setting that up. Then continue.

`scripts/` and `references/` are in this skill's folder. Formats are in
[references/formats.md](references/formats.md).

## Adding a paper

The same rule for a single paper and for papers found in a round.

1. Check for a duplicate: grep the DOI in the reading log. If it is there, say so and stop.
2. Get the abstract: `python3 <skill folder>/scripts/openalex_abstract.py <DOI>`. Exit code 1
   means there is none. A paper without an abstract is only added if it seems promising.
   It then goes on the list of papers the user downloads.
3. Give it a citekey: the first author's last name in lowercase plus the year, like
   `smith2020`. Add `a`, `b` if the log already has it.
4. Write the reading log entry. In a round it goes under the round's heading. A single paper
   goes under `## Single papers`.

## Workflow

One round at a time. Copy this checklist into the chat and tick it off. Stop at step 2 and
step 4 until the user answers.

```
Round progress:
- [ ] 1. Known papers checked
- [ ] 2. Plan agreed
- [ ] 3. Searched and added
- [ ] 4. Full texts downloaded
- [ ] 5. Reading log written
- [ ] 6. Must-reads picked
- [ ] 7. Synthesis written
```

1. **Check what is known.** Grep the reading log.
2. **Plan.** Agree on the question, a few sub-questions, search terms, years, and what is in
   or out. After the go, start the review file with Questions and Plan.
3. **Search and add.** Search OpenAlex. Log each search in the review file. Add papers as in
   "Adding a paper".
4. **Full texts.** List the papers that must be read in full: likely core papers, papers the
   review depends on, and promising papers without an abstract. Fetch the open access ones
   into `pdfs/`. Give the rest to the user with DOI links, to save as `pdfs/<citekey>.pdf`.
5. **Reading log.** One entry per paper. Then fill Papers found in the review file, with each
   paper's relevance for this review.
6. **Must-reads.** One to three papers for the user, foundations first. Each must have been
   read in full.
7. **Synthesis.** Answer the sub-questions in the review file. Check key claims against the
   paper text. If the folder is a git repo, commit.

If nothing good was found, say so. Never pad the list.

## OpenAlex

- Search: `api.openalex.org/works?search=<terms>&filter=publication_year:>2015`. Plain
  `search=` works best. Boolean syntax does not.
- One paper: `api.openalex.org/works/doi:<doi>`. Papers citing it: `works?filter=cites:<id>`.
- Open access PDF: `best_oa_location.pdf_url`.
