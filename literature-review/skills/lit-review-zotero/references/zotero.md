---
tags:
  - ai-generated
---
# Zotero MCP

## Tools

| Task | Tool and arguments |
|---|---|
| Paper by DOI | `mcp__zotero__zotero_advanced_search`, `[{"field": "DOI", "operation": "contains", "value": "<doi>"}]` |
| Paper by citekey | `mcp__zotero__zotero_advanced_search`, `[{"field": "citationKey", "operation": "is", "value": "<citekey>"}]` |
| Paper by author or title | `mcp__zotero__zotero_search_items`, short query like `"Smith 2020"` |
| Papers about a topic | `mcp__zotero__zotero_semantic_search`, `filters={"item_type": "journalArticle"}`, then again with `"preprint"` |
| Metadata and abstract | `mcp__zotero__zotero_get_item_metadata`, `item_key` |
| Highlights | `mcp__zotero__zotero_get_annotations`, always with `item_key` |
| Read part of a paper | `mcp__zotero__zotero_get_pdf_outline`, then `mcp__zotero__zotero_read_pdf_pages`. `format="image"` for equations and figures |
| Add a paper | `mcp__zotero__zotero_add_item`, `source=<DOI>`, `source_type="doi"`, `if_exists="file"`, `collections=[<collection>]` |
| Write a missing abstract | `mcp__zotero__zotero_update_item` |
| New collection | `mcp__zotero__zotero_create_collection` |
| After adding | `mcp__zotero__zotero_update_search_database` |

## Rules

- **Always `if_exists="file"` when adding.** The default `"duplicate"` creates a new item even
  when the DOI is already in the library.
- Ask which collection a paper belongs in, unless a workflow already names it.
- arXiv DOIs (`10.48550/arXiv...`) fail in `mcp__zotero__zotero_add_item`, because it asks
  CrossRef. Add arXiv papers by their arXiv URL with `source_type="url"`.
- If Better BibTeX auto-exports a `.bib` into the repo, commit it together with the reading
  log, so both describe the same library.
- After a bulk add, compare the top-level item count before and after.
- Semantic search without a filter returns highlights first. Filter by item type.
- Query in the field's own words. Items without an abstract are indexed by title only, so
  semantic search is for discovery, not a complete search.
- Do not use `mcp__zotero__zotero_search_by_citation_key`. In web mode it only reads the Extra field
  and misses keys stored in Zotero's citation key field.
- `mcp__zotero__zotero_get_item_fulltext` costs 10K+ tokens per paper. Use it only to read a whole paper.
- Never write notes or summaries into Zotero.
- Never delete items without asking first.
