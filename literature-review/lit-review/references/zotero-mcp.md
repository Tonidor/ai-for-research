---
tags:
  - ai-generated
---
# Using the Zotero MCP

Rule of thumb: the MCP finds and reads papers, the reading log holds judgments.

| Task | Tool and arguments |
|---|---|
| What did we decide about X | Not the MCP. Grep the reading log |
| Papers in the library about a topic | `zotero:zotero_semantic_search`, `filters={"item_type": "journalArticle"}`, then again with `"preprint"` |
| Paper by author or title | `zotero:zotero_search_items`, short query like `"Smith 2020"` |
| Paper by citekey | `zotero:zotero_advanced_search`, `[{"field": "citationKey", "operation": "is", "value": "<citekey>"}]` |
| Metadata and abstract | `zotero:zotero_get_item_metadata`, `item_key` |
| Highlights | `zotero:zotero_get_annotations`, always with `item_key` |
| Read part of a paper | `zotero:zotero_get_pdf_outline`, then `zotero:zotero_read_pdf_pages`. `format="image"` for equations and figures |
| Add a paper | `zotero:zotero_add_item`, `source=<DOI>`, `source_type="doi"`, `if_exists="file"`, `collections=[<round collection>]` |
| After adding | `zotero:zotero_update_search_database` |

Rules:

- **Always `if_exists="file"` when adding.** The default `"duplicate"` creates a new item even
  when the DOI is already in the library.
- After a bulk add, compare the top-level item count before and after.
- Semantic search without a filter returns highlights first. Filter by item type.
- Query in the field's own words. Items without an abstract are indexed by title only. In
  one library tested, 60% of items had no abstract. Treat semantic search as
  discovery, not as a complete search.
- Do not use `zotero:zotero_search_by_citation_key`. In web mode it only reads the Extra field and
  misses keys stored in Zotero's citation key field.
- `zotero:zotero_get_item_fulltext` costs 10K+ tokens per paper. Use it only to read a whole paper.
- Never write notes or summaries into Zotero. They belong in the reading log.
- Never delete items without asking first.
