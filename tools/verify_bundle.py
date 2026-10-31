#!/usr/bin/env python3
"""Verify original PDF integrity and the PDF-only distribution layout."""
import hashlib
import json
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = REPO / "skills/dku-robomaster"


def within(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Path outside skill: " + str(relative))
    return path


def verify(skill=DEFAULT_SKILL):
    skill = Path(skill).resolve()
    for path in skill.rglob("*"):
        if path.is_symlink():
            raise ValueError("Unexpected symbolic link: " + str(path))
        if path.is_file() and path.suffix.lower() == ".txt":
            raise ValueError("Extracted text is not part of this package: " + str(path))
    for relative in ("references/rules-text", "references/wiki-archive"):
        if (skill / relative).exists():
            raise ValueError("Legacy text snapshot directory: " + relative)
    instruction = (skill / "SKILL.md").read_text(encoding="utf-8")
    if not instruction.startswith("---\n") or "name: dku-robomaster\n" not in instruction:
        raise ValueError("Missing expected skill identity")
    for relative in re.findall(r"\]\(([^)]+)\)", instruction):
        if "://" not in relative and not relative.startswith("#"):
            if not within(skill, relative.split("#", 1)[0]).is_file():
                raise ValueError("Missing Skill reference: " + relative)
    catalog = json.loads((skill / "references/bundled-library.json").read_text(encoding="utf-8"))
    if catalog.get("format") != "original-pdf" or "wiki_manifest" in catalog:
        raise ValueError("Expected the original-PDF catalogue format")
    rules = catalog["rules"]
    core = catalog["core_documents"]
    if not rules or not core:
        raise ValueError("Missing PDF catalogue entries")
    declared = set()
    for record in rules + core:
        if "extracted_text" in record:
            raise ValueError("Legacy extracted-text catalogue entry")
        path = within(skill, record["original"])
        data = path.read_bytes()
        if path in declared or path.suffix.lower() != ".pdf":
            raise ValueError("Duplicate or invalid PDF: " + record["original"])
        declared.add(path)
        if not data.startswith(b"%PDF-"):
            raise ValueError("Not a PDF: " + record["original"])
        if len(data) != record["size_bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
            raise ValueError("PDF integrity mismatch: " + record["original"])
    if declared != {p.resolve() for p in (skill / "assets").rglob("*.pdf")}:
        raise ValueError("PDF files and catalogue do not match")
    for script in (skill / "scripts").glob("*.py"):
        compile(script.read_text(encoding="utf-8"), str(script), "exec")
    return {"pdfs": len(declared), "rules_pdfs": len(rules),
            "core_pdfs": len(core), "text_files": 0,
            "files": sum(p.is_file() for p in skill.rglob("*"))}


if __name__ == "__main__":
    try:
        print(json.dumps({"ok": True, **verify()}, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
        print("Verification failed: " + str(error), file=sys.stderr)
        sys.exit(1)
