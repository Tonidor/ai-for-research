---
name: zotero
description: Works with a Zotero library through the Zotero MCP. Checks for duplicates, adds papers by DOI, finds papers by citekey, DOI, author or topic, and reads PDFs and highlights. Use when the user mentions Zotero, their library, a citekey or highlights, or when another skill such as lit-review stores or reads papers.
tags:
  - ai-generated
---
# Zotero

## Requires

If one is missing, say so and stop.

- **Zotero MCP**, registered as `zotero`. Check with `zotero:zotero_write_capabilities`.
- **Better BibTeX**, for citekeys. Check that an item added more than a day ago shows a
  `citationKey` in `zotero:zotero_get_item_metadata` with `format="json"`.

## With lit-review

The `lit-review` skill hands over at four points.

- **Duplicate check:** also search the library by DOI. If the paper is there but not in the
  reading log, say which collections it is in and offer to write the log entry.
- **Adding a paper:** add it with `if_exists="file"` into the round's collection, or ask which
  collection for a single paper. Put its Zotero key in the reading log entry, and use its
  `citationKey` as the citekey.
- **The round's collection:** create it after the user says go, named after the round.
- **Full texts:** the user saves them with the Zotero Connector onto the item, not into
  `pdfs/`. Read them through the tools below.

A paper added through the API has an empty `citationKey` until Zotero desktop syncs and
Better BibTeX assigns one. Meanwhile use the lit-review citekey rule, and after the sync check
that the keys match.

## Tools

| Task | Tool and arguments |
|---|---|
| Paper by DOI | `zotero:zotero_advanced_search`, `[{"field": "DOI", "operation": "contains", "value": "<doi>"}]` |
| Paper by citekey | `zotero:zotero_advanced_search`, `[{"field": "citationKey", "operation": "is", "value": "<citekey>"}]` |
| Paper by author or title | `zotero:zotero_search_items`, short query like `"Smith 2020"` |
| Papers about a topic | `zotero:zotero_semantic_search`, `filters={"item_type": "journalArticle"}`, then again with `"preprint"` |
| Metadata and abstract | `zotero:zotero_get_item_metadata`, `item_key` |
| Highlights | `zotero:zotero_get_annotations`, always with `item_key` |
| Read part of a paper | `zotero:zotero_get_pdf_outline`, then `zotero:zotero_read_pdf_pages`. `format="image"` for equations and figures |
| Add a paper | `zotero:zotero_add_item`, `source=<DOI>`, `source_type="doi"`, `if_exists="file"`, `collections=[<collection>]` |
| Write a missing abstract | `zotero:zotero_update_item` |
| New collection | `zotero:zotero_create_collection` |
| After adding | `zotero:zotero_update_search_database` |

## Rules

- **Always `if_exists="file"` when adding.** The default `"duplicate"` creates a new item even
  when the DOI is already in the library.
- Ask which collection a paper belongs in, unless a workflow already names it.
- After a bulk add, compare the top-level item count before and after.
- Semantic search without a filter returns highlights first. Filter by item type.
- Query in the field's own words. Items without an abstract are indexed by title only, so
  semantic search is for discovery, not a complete search.
- Do not use `zotero:zotero_search_by_citation_key`. In web mode it only reads the Extra field
  and misses keys stored in Zotero's citation key field.
- `zotero:zotero_get_item_fulltext` costs 10K+ tokens per paper. Use it only to read a whole paper.
- Never write notes or summaries into Zotero.
- Never delete items without asking first.
