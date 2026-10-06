---
tags:
  - ai-generated
---
# Formats

## Reading log

One file, `reading-log.md`, one entry per paper. This is where judgments live. The paper
itself is in `pdfs/`, the log holds what it means for the project.

```markdown
### [citekey] Short title
DOI: 10.1234/abcd · Source: full text · 2026-09-14
- Problem: what gap the paper addresses.
- Approach: the setup, with the numbers a model needs.
- Finding: the result, with numbers.
- Relevance: what it means for the project, and what it rules in or out.
```

- **Source:** `full text` or `abstract`, what the entry was written from.
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
Start it after the plan is agreed, with Questions and Plan, and fill in the rest as the
round goes. It holds everything about the round except the per-paper detail, which stays in
the reading log.

```markdown
---
type: review
date: 2026-10-05
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
- No abstract, on the download list: [doe2019]

## Papers found

Grouped by sub-question. Each paper gets its relevance for this review: core, supporting or
peripheral, and why in one line.

1. Sub-question one
   - [smith2020] core: gives the method the question depends on.
   - [lee2023] supporting: a second dataset, smaller.
2. Sub-question two
   - [kim2021] peripheral: background only.

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
