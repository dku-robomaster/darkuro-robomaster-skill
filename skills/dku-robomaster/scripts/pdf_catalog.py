#!/usr/bin/env python3
"""Locate bundled original PDFs by filename and catalogue metadata."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def load():
    catalog = json.loads((ROOT / "references/bundled-library.json").read_text(encoding="utf-8"))
    records = []
    for key, category in (("rules", "rules"), ("core_documents", "core")):
        for item in catalog.get(key, []):
            path = (ROOT / item["original"]).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                raise ValueError("Missing or invalid PDF path: " + item["original"])
            year = re.search(r"20\d{2}", item["name"])
            version = re.search(r"V\d+(?:\.\d+)*", item["name"])
            records.append({
                "name": item["name"], "category": category,
                "season_in_filename": int(year.group()) if year else None,
                "version_in_filename": version.group() if version else None,
                "relative_path": item["original"], "pdf_path": str(path),
                "size_bytes": item["size_bytes"], "sha256": item["sha256"]
            })
    records.sort(key=lambda r: (-(r["season_in_filename"] or 0), r["name"]))
    return records, catalog["bundled_at"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    listing = sub.add_parser("list")
    listing.add_argument("--limit", type=int, default=30)
    finding = sub.add_parser("find")
    finding.add_argument("terms", nargs="+")
    finding.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    try:
        records, date = load()
        if args.command == "find":
            terms = [term.casefold() for term in args.terms]
            records = [r for r in records if all(t in (r["name"] + " " + r["relative_path"]).casefold() for t in terms)]
        result = {"bundled_at": date, "total_matches": len(records),
                  "results": records[:max(1, min(args.limit, 100))],
                  "next_step": "Open pdf_path with a PDF reader; this catalogue does not search document bodies."}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
