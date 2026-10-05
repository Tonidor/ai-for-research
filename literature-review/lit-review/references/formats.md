---
tags:
  - ai-generated
---
# Formats

## Reading log

One file, `reading-log.md`, one entry per paper. This is where judgments live. The paper
itself is in Zotero or `pdfs/`, the log holds what it means for the project.

```markdown
### [citekey] Short title
DOI: 10.1234/abcd · Zotero: ITEMKEY · Tier: core · Source: full PDF · 2026-09-14
- Problem: what gap the paper addresses.
- Approach: the setup, with the numbers a model needs.
- Finding: the result, with numbers. Check this one against the PDF.
- Relevance: what it means for the project, and what it rules in or out.
```

- **DOI:** always. **Zotero:** the item key, only when the paper is in Zotero.
- **Tier:** `core`, `supporting`, `peripheral`, or `unsorted` until decided. Only the user
  decides. Default meanings:
  - **core**: the project cannot go ahead without it. It gives a number, mechanism, method or
    dataset the work must build on or be checked against.
  - **supporting**: shapes a choice, a parameter range or a design, but the work could go
    ahead without it.
  - **peripheral**: context only. Motivation or related work.

  At the first round, write these at the top of the log, adapted to the project with the
  user. From then on the log's version is the one that counts.
- **Source:** what the bullets were written from. `full PDF`, `full text`, `partial text`,
  `abstract + PDF spot check`, `abstract`, or `unknown`. It says how far to trust the entry.
- **Date:** the date of the review round, or the date added for a single paper.
- Group entries by review round, one `##` section per round. Under the heading, only a link
  to the round's review file:
  ```markdown
  ## Priming

  Review: `reviews/priming.md`
  ```
  The question, plan and search log live in the review file, not here.
- Papers added outside a round go under one `## Single papers` section at the end, with the
  date they were added.
- Claude greps the log. It never loads the whole file.

## Review file

One file per round in `reviews/`, named after the round, for example `reviews/priming.md`.
Start it at step 1 with Questions and Plan, and fill in the rest as the round goes. It holds
everything about the round except the per-paper detail, which stays in the reading log.

```markdown
---
type: review
date: 2026-10-05
zotero_collection: Priming (ABCD1234)   # only with Zotero
papers: [smith2020, lee2023, kim2021]
---
# Priming review

## Questions

Main question in one sentence.

1. Sub-question one.
2. Sub-question two.

## Plan

- Search terms: `term one`, `term two`
- Venues and years: journals, conferences, 2015 onward
- In: what makes a paper relevant
- Out: what excludes it

## Search log

- OpenAlex, `term one`, 2015 onward, 214 hits, 12 added
- Snowball, papers citing [smith2020], 31 hits, 4 added
- Skipped: [doe2019], no abstract available

## Papers found

1. Sub-question one: [smith2020] Short title, [lee2023] Short title
2. Sub-question two: [kim2021] Short title

## Must-reads

1. [smith2020], foundation. Why it is needed, in one line.
2. [lee2023], detail. Why it is needed, in one line.

## Synthesis

**Answers.**
1. Sub-question one: the answer in a few sentences, citing [citekey].
2. Sub-question two: the answer, or "not answered by the literature found".

**Contradictions.** Where papers disagree, and why.

**Gaps.** What the literature does not answer, and what the gap search turned up.
```

- `papers` lists every citekey added in this round. Papers from earlier rounds may be cited
  in the Synthesis without being listed.
- The Synthesis stays short. Detail belongs in the reading log entries it cites.
