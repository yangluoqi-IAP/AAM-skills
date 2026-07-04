"""Extract lightweight structural patterns from local JAMES PDF samples.

The script intentionally stores only metadata, short abstracts/key points, and
section headings. It is meant to refresh the skill's style references without
embedding full copyrighted article text.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader


SECTION_PATTERNS = [
    "abstract",
    "plain language summary",
    "key points",
    "introduction",
    "data",
    "methods",
    "method",
    "model",
    "experimental design",
    "experiments",
    "results",
    "discussion",
    "conclusions",
    "conclusion",
    "open research",
    "data availability",
    "code availability",
    "acknowledgments",
    "references",
]


def normalize(text: str) -> str:
    text = text.replace("\u2010", "-").replace("\u2011", "-").replace("\u2013", "-")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def read_first_pages(path: Path, max_pages: int = 4) -> str:
    reader = PdfReader(str(path))
    chunks = []
    for page in reader.pages[: min(max_pages, len(reader.pages))]:
        try:
            chunks.append(page.extract_text() or "")
        except Exception as exc:  # pragma: no cover - PDF extraction is messy
            chunks.append(f"[extraction error: {exc}]")
    return normalize("\n".join(chunks))


def read_all_pages_for_headings(path: Path, max_pages: int = 30) -> str:
    reader = PdfReader(str(path))
    chunks = []
    for page in reader.pages[: min(max_pages, len(reader.pages))]:
        try:
            chunks.append(page.extract_text() or "")
        except Exception:
            continue
    return normalize("\n".join(chunks))


def clean_line(line: str) -> str:
    line = re.sub(r"\s+", " ", line).strip()
    line = re.sub(r"^\d+(\.\d+)*\.?\s+", "", line)
    return line.strip(" .")


def find_title(front: str, fallback: str) -> str:
    lines = [clean_line(x) for x in front.splitlines() if clean_line(x)]
    skip = {
        "research article",
        "journal of advances in modeling earth systems",
        "james",
        "key points:",
        "plain language summary",
        "abstract",
    }
    candidates = []
    for line in lines[:80]:
        low = line.lower()
        if low in skip or low.startswith("10.") or "doi.org" in low:
            continue
        if any(x in low for x in ["received", "accepted", "published", "citation:", "author", "copyright"]):
            continue
        if 35 <= len(line) <= 180 and sum(c.isalpha() for c in line) > 20:
            candidates.append(line)
    if candidates:
        return candidates[0]
    return fallback


def extract_between(text: str, start_patterns: list[str], stop_patterns: list[str], max_chars: int) -> str:
    low = text.lower()
    starts = []
    for pat in start_patterns:
        match = re.search(rf"\b{re.escape(pat)}\b[:\s]*", low)
        if match:
            starts.append(match.end())
    if not starts:
        return ""
    start = min(starts)
    stops = []
    for pat in stop_patterns:
        match = re.search(rf"\n\s*{re.escape(pat)}\b[:\s]*", low[start:])
        if match:
            stops.append(start + match.start())
    end = min(stops) if stops else min(len(text), start + max_chars)
    snippet = normalize(text[start:end])
    return snippet[:max_chars].strip()


def extract_key_points(front: str) -> list[str]:
    block = extract_between(
        front,
        ["key points"],
        ["plain language summary", "abstract", "1 introduction", "introduction"],
        1800,
    )
    if not block:
        return []
    raw_items = re.split(r"\n\s*[\u2022\-]\s+|\n(?=[A-Z][^.\n]{20,160}$)", block)
    items = []
    for item in raw_items:
        item = normalize(item)
        item = re.sub(r"^[:\-\u2022]\s*", "", item)
        if 20 <= len(item) <= 260 and item.lower() not in {"key points"}:
            items.append(item)
    return items[:5]


def extract_headings(full_text: str) -> list[str]:
    headings: list[str] = []
    seen = set()
    for raw in full_text.splitlines():
        line = clean_line(raw)
        lowered = line.lower()
        for special in ("abstract", "plain language summary", "key points", "data availability statement"):
            if lowered.startswith(special + " "):
                line = special.title()
                lowered = line.lower()
                break
        if not line or len(line) > 110:
            continue
        low = lowered
        if low in seen:
            continue
        is_numbered = bool(re.match(r"^\d+(\.\d+)*\s+[A-Z]", raw.strip()))
        is_known = any(low == pat or low.startswith(pat + " ") for pat in SECTION_PATTERNS)
        if is_numbered or is_known:
            if not any(x in low for x in ["figure ", "table ", "citation", "doi", "page "]):
                headings.append(line)
                seen.add(low)
    return headings[:30]


def summarize_pdf(path: Path) -> dict[str, object]:
    front = read_first_pages(path)
    full = read_all_pages_for_headings(path)
    abstract = extract_between(
        front,
        ["abstract"],
        ["plain language summary", "key points", "1 introduction", "introduction"],
        1400,
    )
    plain_language_summary = extract_between(
        front,
        ["plain language summary"],
        ["abstract", "key points", "1 introduction", "introduction"],
        1000,
    )
    key_points = extract_key_points(front)
    return {
        "file": path.name,
        "title": find_title(front, path.stem),
        "has_abstract": bool(abstract),
        "has_plain_language_summary": bool(plain_language_summary),
        "key_point_count": len(key_points),
        "headings": extract_headings(full),
    }


def write_markdown(records: list[dict[str, object]], output: Path) -> None:
    lines = [
        "# JAMES Sample Extraction",
        "",
        "This file is generated by `scripts/extract_james_patterns.py` and stores",
        "only lightweight article metadata and structural cues.",
        "",
    ]
    for record in records:
        lines.extend(
            [
                f"## {record['title']}",
                "",
                f"- File: `{record['file']}`",
            ]
        )
        lines.append(f"- Has abstract: {record.get('has_abstract')}")
        lines.append(f"- Has plain language summary: {record.get('has_plain_language_summary')}")
        lines.append(f"- Detected key point count: {record.get('key_point_count')}")
        headings = record.get("headings") or []
        if headings:
            lines.append("- Detected headings: " + "; ".join(str(x) for x in headings[:18]))
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_dir", type=Path)
    parser.add_argument("--json", type=Path, default=Path("references/james-sample-extraction.json"))
    parser.add_argument("--markdown", type=Path, default=Path("references/james-sample-extraction.md"))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument(
        "--match",
        action="append",
        default=[],
        help="Case-insensitive regex applied to file names before extraction. May be repeated.",
    )
    args = parser.parse_args()

    pdfs = sorted(args.pdf_dir.glob("*.pdf"))
    if args.match:
        patterns = [re.compile(item, re.IGNORECASE) for item in args.match]
        pdfs = [path for path in pdfs if any(pattern.search(path.name) for pattern in patterns)]
    if args.limit:
        pdfs = pdfs[: args.limit]
    records = [summarize_pdf(path) for path in pdfs]
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(records, args.markdown)
    print(f"Extracted {len(records)} PDFs")
    print(args.json)
    print(args.markdown)


if __name__ == "__main__":
    main()
