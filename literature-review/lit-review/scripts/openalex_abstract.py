"""Print a paper's abstract from OpenAlex, given its DOI.

OpenAlex stores abstracts as an inverted index, a map from each word to its positions.
This rebuilds the plain text. Exit code 1 means OpenAlex has no abstract for the DOI.

Usage: python3 openalex_abstract.py 10.1111/ele.12205
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

KEY_FILE = Path.home() / ".config/openalex/api-key"

doi = sys.argv[1].removeprefix("https://doi.org/")
request = urllib.request.Request(f"https://api.openalex.org/works/doi:{doi}")
if KEY_FILE.exists():
    request.add_header("Authorization", f"Bearer {KEY_FILE.read_text().strip()}")

try:
    with urllib.request.urlopen(request) as response:
        work = json.load(response)
except urllib.error.HTTPError as error:
    sys.exit(f"OpenAlex returned {error.code} for {doi}")

index = work.get("abstract_inverted_index")
if not index:
    sys.exit(f"No abstract in OpenAlex for {doi}")

positions = {pos: word for word, places in index.items() for pos in places}
print(" ".join(positions[i] for i in sorted(positions)))
