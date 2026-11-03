#!/usr/bin/env python3
"""Check prose against the countable rules of Simplified Research English.

Usage:
    check.py FILE [FILE ...] [--mode descriptive|procedural|mixed] [--notes] [--no-hints]
             [--dictionary PATH]
    check.py -            (read Markdown from stdin)

Reads Markdown, LaTeX (.tex), HTML (.html), or plain text. It skips code, math,
headings, tables, URLs, and citations. Each finding is one line:

    path:line: ERROR|HINT RULE message | sentence excerpt

The rule numbers are the numbers in references/writing-rules.md. An ERROR breaks
a rule. A HINT needs a human decision. The exit code is 1 if there is an error.
The script does not check meaning: rules such as 4.1, 2.1, GR-3, R1, R2, and R4
need a careful read. The checks of verbs, contractions, and modals adapt
ste_check.py of 0xpili/simplified-technical-english (MIT license).
"""
import argparse
import html
import re
import sys
from pathlib import Path

DEFAULT_DICTIONARY = Path(__file__).resolve().parent.parent / "references" / "dictionary.md"
BREAK = "\x00"  # block separator that does not change line numbers
SOFT = "\x02"  # a removed line break inside a sentence; counts as a line
ABBREVIATIONS = ["et al.", "e.g.", "i.e.", "etc.", "vs.", "cf.", "Fig.", "Figs.", "Eq.", "Eqs.",
                 "Sec.", "Ch.", "Tab.", "No.", "Dr.", "Prof.", "Ref.", "Refs.", "approx."]
UNITS = r"(?:%|ms|s|min|h|km|m|kg|USD|CHF|EUR)"
ALLOWED_IN_NOTES = {"might"}  # rule 3.2: working notes can use "might" for open speculation
# rule 3.5: the approved "-ing" words of STE. The technical names in the dictionary are also permitted.
ING_APPROVED = {"mating", "missing", "remaining", "lighting", "opening", "routing", "servicing", "during"}
ING_NOT_SUFFIX = {"ring", "spring", "string", "king", "thing", "wing", "sing", "bring", "sting", "swing",
                  "nothing", "anything", "everything", "something", "bearing", "ceiling", "morning",
                  "evening", "according"}
MODALS = {"should", "would", "may", "might", "shall", "ought"}  # rule 3.2: only can, must, will
PARTICIPLE = (r"(?:\w+ed|given|shown|known|taken|chosen|drawn|made|found|seen|done|written|built|run|set|"
              r"kept|held|paid|sent|won|lost|proven|broken|hidden|driven|put|left|told|brought|bought|"
              r"thought|sold|spent)")
BARE_THIS = re.compile(
    r"\b(this|these)\b(?=\s*[.,;:)]|\s+(?:is|are|was|were|can|will|shows?|suggests?|means|implies|imply|"
    r"leads?|makes?|gives?|allows?|holds?|happens?|requires?|explains?|ensures?|yields?|causes?)\b)",
    re.IGNORECASE)
CONTRACTION = re.compile(r"\b\w+n['\u2019]t\b|\b\w+['\u2019](?:re|ll|ve|m|d)\b|"
                         r"\b(?:it|that|there|what|let|who|here|he|she)['\u2019]s\b", re.IGNORECASE)
HAVE_PARTICIPLE = re.compile(rf"\b(?:has|have|had)\s+(?:been|{PARTICIPLE})\b", re.IGNORECASE)
COMPLEX_PASSIVE = re.compile(rf"\b(?:can|will|must|could|would|should|may|might|shall)\s+(?:not\s+)?be\s+"
                             rf"(?:\w+ly\s+)?{PARTICIPLE}\b|\b(?:is|are|was|were)\s+to\s+be\s+{PARTICIPLE}\b",
                             re.IGNORECASE)
PASSIVE_BY = re.compile(rf"\b(?:is|are|was|were|be|been|being)\s+(?:\w+\s+)?{PARTICIPLE}\s+by\b", re.IGNORECASE)
PASSIVE = re.compile(rf"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?{PARTICIPLE}\b", re.IGNORECASE)
BE_ING = re.compile(r"\b(?:is|are|was|were|be|been|am)\s+(\w+ing)\b", re.IGNORECASE)
STRUCTURE = [(CONTRACTION, "4.2", "contraction"),
             (HAVE_PARTICIPLE, "3.4", "perfect tense"),
             (COMPLEX_PASSIVE, "3.4", "complex passive"),
             (PASSIVE_BY, "3.6", "passive voice")]


def blank(match):
    """Replace a match with the same number of newlines, so line numbers stay correct."""
    return "\n" * match.group(0).count("\n")


def load_dictionary(path):
    """Return ({phrase: (write_instead, is_hint, is_exact)}, technical_ing).

    The first part comes from each table with a 'Do not use' column. An item in backticks,
    for example `karma`, matches only with that exact case. The second part is the set of
    "-ing" words in the first column of all tables, for example "bidding" (rule 3.5).
    """
    entries, technical_ing, header = {}, set(), None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if not "".join(cells).strip("-: "):
            continue
        technical_ing.update(w for w in re.findall(r"[a-z]+(?:-[a-z]+)*", cells[0].lower()) if w.endswith("ing"))
        if "do not use" not in header:
            continue
        column = header.index("do not use")
        preferred = cells[0].replace("*", "").replace("`", "")
        for item in (cells[column] if column < len(cells) else "").split(","):
            item = item.strip()
            hint = item.endswith("?")
            item = item.rstrip("?").strip()
            exact = len(item) > 2 and item.startswith("`") and item.endswith("`")
            item = item.strip("`")
            if item:
                entries[item if exact else item.lower()] = (preferred, hint, exact)
    return entries, technical_ing


def phrase_pattern(phrase, exact=False):
    """Match a phrase as whole words. A one-word entry also matches its usual inflections."""
    if " " not in phrase and phrase.isalpha():
        stem = phrase[:-1] if phrase.endswith("e") else phrase
        body = rf"(?:{re.escape(phrase)}(?:s|es|d|ed)?|{re.escape(stem)}ing)"
    else:
        body = re.escape(phrase)
    return re.compile(rf"(?<![\w-]){body}(?![\w-])", 0 if exact else re.IGNORECASE)


def math_token(match):
    """Replace display math with one word. Keep the period if the formula ends the sentence."""
    body = match.group(0)
    inner = re.sub(r"(\$\$|\\\]|\\end\{[^}]*\})\s*$", "", body.rstrip())
    inner = re.sub(r"\\(?:label|tag)\{[^}]*\}|\\nonumber|\\notag|\\\\", "", inner)
    return SOFT * body.count("\n") + " MATH" + ("." if inner.rstrip().endswith(".") else "") + " "


def common_cleanup(text):
    text = text.replace("\\$", "USD")
    text = re.sub(r"\$\$.*?\$\$|\\\[.*?\\\]", math_token, text, flags=re.S)
    text = re.sub(r"\$[^$\n]+\$|\\\(.*?\\\)", "MATH", text, flags=re.S)
    return re.sub(r"https?://[^\s)>\]]+", "URL", text)


def markdown_to_text(text):
    text = re.sub(r"\A---\n.*?\n---\n", blank, text, flags=re.S)
    text = re.sub(r"^(```|~~~).*?^\1[^\n]*$", blank, text, flags=re.S | re.M)
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    text = common_cleanup(text)
    lines = []
    for line in text.split("\n"):
        if re.match(r"\s*(#|\|)", line):
            line = BREAK
        elif re.match(r"\s*([-*+]|\d+[.)])\s+", line):
            line = BREAK + re.sub(r"\s*([-*+]|\d+[.)])\s+", "", line, count=1)
        lines.append(re.sub(r"^\s*>\s?", "", line))
    text = "\n".join(lines)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"!?\[\[[^\]]*\]\]", "LINK", text)  # a wiki-link is a title: one word (rule 8.6)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`[^`]+`", "CODE", text)
    text = re.sub(r"\*{1,3}", "", text)
    return re.sub(r"(?<!\w)_{1,3}(?=\w)|(?<=\w)_{1,3}(?!\w)", "", text)


def tex_to_text(text):
    text = re.sub(r"(?<!\\)%.*", "", text)
    if "\\begin{document}" in text:
        head, _, body = text.partition("\\begin{document}")
        text = "\n" * head.count("\n") + body
    math_envs = r"equation|align|gather|multline|eqnarray|displaymath"
    other_envs = r"tabular|tikzpicture|verbatim|lstlisting"
    text = re.sub(rf"\\begin\{{({math_envs})\*?\}}.*?\\end\{{\1\*?\}}", math_token, text, flags=re.S)
    text = re.sub(rf"\\begin\{{({other_envs})\*?\}}.*?\\end\{{\1\*?\}}", lambda m: BREAK + blank(m),
                  text, flags=re.S)
    text = common_cleanup(text)
    text = re.sub(r"\\(?:sub)*(?:section|chapter|paragraph)\*?(?:\[[^\]]*\])?\{[^}]*\}", BREAK, text)
    text = re.sub(r"\\(?:caption|footnote)\*?(?:\[[^\]]*\])?\{([^{}]*)\}", BREAK + r"\1" + BREAK, text)
    text = re.sub(r"\\(?:cite[a-z]*|ref|eqref|cref|Cref|autoref)\{[^}]*\}", "CITE", text)
    text = re.sub(r"\\label\{[^}]*\}", "", text)
    text = re.sub(r"\\(?:begin|end)\{[^}]*\}|\\item\b|\\\\", BREAK, text)
    for _ in range(3):
        text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    return text.replace("~", " ").replace("``", "\u201c").replace("''", "\u201d").replace("{", "").replace("}", "")


def html_to_text(text):
    text = re.sub(r"<(script|style|svg|pre|code|math|table)\b.*?</\1>", lambda m: BREAK + blank(m), text,
                  flags=re.S | re.I)
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    text = re.sub(r"<(h[1-6])\b.*?</\1>", lambda m: BREAK + blank(m), text, flags=re.S | re.I)
    text = re.sub(r"</?(p|div|li|ul|ol|section|header|footer|figure|figcaption|blockquote|br|tr|td|th|"
                  r"details|summary|nav|main|article|dd|dt)\b[^>]*>", BREAK, text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    return common_cleanup(html.unescape(text))


def blocks(text):
    """Yield (first_line, block_text) for each prose block."""
    line = 1
    for chunk in re.split(rf"(\n\s*\n|{BREAK})", text):
        if chunk and chunk != BREAK and chunk.strip():
            if not re.fullmatch(r"\s*(MATH|CODE|CITE)?\s*", chunk):
                lead = len(chunk) - len(chunk.lstrip("\n"))
                yield line + lead, chunk.strip()
        line += chunk.count("\n") + chunk.count(SOFT)


def sentences(block):
    """Yield (offset, sentence). Abbreviations and decimals do not end a sentence."""
    protected = block
    for abbreviation in ABBREVIATIONS:
        protected = protected.replace(abbreviation, abbreviation.replace(".", "\x01"))
    protected = re.sub(r"\b([A-Z])\.(?=\s+[A-Z])", "\\1\x01", protected)  # initials
    ends = [m.end() for m in re.finditer(r"[.!?](?:[\"\u201d')\]]*)(?=\s+[A-Z0-9(\"\u201c$]|\s*$)", protected)]
    start = 0
    for end in ends + [len(block)]:
        segment = block[start:end]
        if segment.strip():
            yield start + len(segment) - len(segment.lstrip()), segment.strip()
        start = end


def word_count(sentence):
    text = sentence
    while re.search(r"\([^()]*\)", text):
        text = re.sub(r"\([^()]*\)", " PAREN ", text)
    text = re.sub(rf"\b\d[\d.,]*\s?{UNITS}(?!\w)", "NUMBER", text)
    return len([t for t in text.split() if re.search(r"[A-Za-z0-9]", t)])


def check_file(path, label, args, dictionary, technical_ing):
    raw = sys.stdin.read() if label == "-" else path.read_text(encoding="utf-8")
    suffix = "" if label == "-" else path.suffix.lower()
    if suffix in (".html", ".htm"):
        text = html_to_text(raw)
    elif suffix == ".tex":
        text = tex_to_text(raw)
    else:
        text = markdown_to_text(raw)
    patterns = [(phrase, phrase_pattern(phrase, exact), preferred, hint, exact)
                for phrase, (preferred, hint, exact) in dictionary.items()
                if not (args.notes and phrase in ALLOWED_IN_NOTES)]
    modals = MODALS - set(dictionary)  # the dictionary already reports the other modals
    ing_permitted = ING_APPROVED | ING_NOT_SUFFIX | technical_ing
    limit = 20 if args.mode == "procedural" else 25
    length_rule = "5.1" if args.mode == "procedural" else "6.3"
    findings = []

    def add(line, level, rule, message, sentence):
        excerpt = re.sub(r"\s+", " ", sentence)
        findings.append((line, level, rule, message, excerpt[:90] + ("..." if len(excerpt) > 90 else "")))

    for first_line, block in blocks(text):
        found = list(sentences(block))
        if len(found) > 6:
            add(first_line, "ERROR", "6.6", f"paragraph has {len(found)} sentences (max 6)", found[0][1])
        for offset, sentence in found:
            line = first_line + block[:offset].count("\n") + block[:offset].count(SOFT)
            sentence = sentence.replace(SOFT, "")
            # quoted text is a mention, not a use, and counts as one word (rule 8.6)
            plain = re.sub(r'"[^"]*"|\u201c[^\u201d]*\u201d', " QUOTE ", sentence)
            words = word_count(plain)
            if words > limit:
                add(line, "ERROR", length_rule, f"{words} words (max {limit})", sentence)
            elif words > 20 and args.mode == "mixed" and not args.no_hints:
                add(line, "HINT", "5.1", f"{words} words (max 20 if procedural)", sentence)
            if ";" in plain:
                add(line, "ERROR", "8.1", "semicolon", sentence)
            for pattern, rule, message in STRUCTURE:
                match = pattern.search(plain)
                if match and not (pattern is PASSIVE_BY and COMPLEX_PASSIVE.search(plain)):
                    add(line, "ERROR", rule, f'{message} "{match.group(0)}"', sentence)
            progressive = {m.group(1).lower() for m in BE_ING.finditer(plain)} - ing_permitted
            if progressive:
                add(line, "ERROR", "3.5", f'progressive form "{", ".join(sorted(progressive))}"', sentence)
            for match in BARE_THIS.finditer(plain):
                add(line, "ERROR", "GR-4", f'"{match.group(1)}" without a noun', sentence)
            for word in sorted({w for w in re.findall(r"[A-Za-z]+", plain) if w.lower() in modals}):
                add(line, "ERROR", "3.2", f'"{word}": use "can", "must", "will", or an evidence word', sentence)
            for phrase, pattern, preferred, hint, exact in patterns:
                if hint and args.no_hints:
                    continue
                for match in pattern.finditer(plain):
                    word = match.group(0)
                    if not exact and word[0].isupper() and match.start() > 0 and phrase[0].islower():
                        continue  # a proper noun, for example the month "May"
                    add(line, "HINT" if hint else "ERROR", "dictionary",
                        f'"{word}": write {preferred}', sentence)
            if args.no_hints:
                continue
            if PASSIVE.search(plain) and not (PASSIVE_BY.search(plain) or COMPLEX_PASSIVE.search(plain)):
                add(line, "HINT", "3.6", f'possible passive voice "{PASSIVE.search(plain).group(0)}"', sentence)
            if re.search(r"\bcould\b", plain, re.IGNORECASE):
                add(line, "HINT", "3.2", '"could" only as the past tense of "can"', sentence)
            ing = {w for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", plain)
                   if w.lower().endswith("ing") and len(w) > 4 and not w.isupper()}
            ing = {w for w in ing if w.lower() not in ing_permitted | progressive}
            if ing:
                add(line, "HINT", "3.5", f'"-ing" form outside a technical name: {", ".join(sorted(ing))}',
                    sentence)
    for line, level, rule, message, excerpt in sorted(findings, key=lambda f: (f[1] != "ERROR", f[0])):
        print(f"{label}:{line}: {level} {rule} {message} | {excerpt}")
    return sum(1 for f in findings if f[1] == "ERROR"), len(findings)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="+", help="files to check, or - for stdin")
    parser.add_argument("--mode", choices=["descriptive", "procedural", "mixed"], default="descriptive",
                        help="text type: 25 words (descriptive), 20 words (procedural), or 25 with hints over 20")
    parser.add_argument("--notes", action="store_true", help="working notes: allow \"might\" (rule 3.2)")
    parser.add_argument("--no-hints", action="store_true", help="show errors only")
    parser.add_argument("--dictionary", type=Path, default=DEFAULT_DICTIONARY)
    args = parser.parse_args()
    dictionary, technical_ing = load_dictionary(args.dictionary)
    errors = total = 0
    for name in args.files:
        e, t = check_file(Path(name), name, args, dictionary, technical_ing)
        errors, total = errors + e, total + t
    print(f"{errors} errors, {total - errors} hints", file=sys.stderr)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
