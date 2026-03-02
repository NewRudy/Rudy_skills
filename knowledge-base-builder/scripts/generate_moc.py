#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MOC (Map of Content) Generator
Scans vault and generates/updates MOC index files.
Usage: python generate_moc.py [vault_path]
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return {}

    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm

def scan_vault(vault_path):
    """Scan vault and collect note metadata."""
    vault = Path(vault_path)
    notes = {}

    for md_file in sorted(vault.rglob("*.md")):
        rel = md_file.relative_to(vault)

        # Skip hidden, tools, output dirs
        parts = rel.parts
        if any(p.startswith(".") or p.startswith("_") or p in ("tools", "FINAL_PACKAGE", "node_modules") for p in parts):
            continue

        # Skip MOC files themselves and README
        if md_file.stem.startswith("_") and md_file.stem.endswith("_MOC"):
            continue

        fm = extract_frontmatter(md_file)
        domain = parts[0] if len(parts) > 1 else "root"

        notes.setdefault(domain, []).append({
            "path": rel,
            "stem": md_file.stem,
            "title": fm.get("title", md_file.stem),
            "status": fm.get("status", "unknown"),
            "importance": fm.get("importance", "unknown"),
            "tags": fm.get("tags", ""),
        })

    return notes

def generate_domain_moc(domain, domain_notes, vault_path):
    """Generate MOC for a single domain folder."""
    today = datetime.now().strftime("%Y-%m-%d")

    # Extract domain display name
    domain_name = re.sub(r'^\d+-', '', domain)

    content = f"""---
title: "{domain_name} - 知识导图"
type: moc
tags: [MOC, 索引]
updated: {today}
---

# {domain_name} - 知识导图

## 知识结构

"""
    # Group by status
    final_notes = [n for n in domain_notes if n["status"] == "final"]
    draft_notes = [n for n in domain_notes if n["status"] != "final"]

    if final_notes:
        content += "### 已完成\n"
        for note in final_notes:
            content += f"- [[{note['stem']}]] {'*' if note['importance'] == 'high' else ''}\n"
        content += "\n"

    if draft_notes:
        content += "### 待完善\n"
        for note in draft_notes:
            content += f"- [[{note['stem']}]]\n"
        content += "\n"

    # Stats
    total = len(domain_notes)
    done = len(final_notes)
    content += f"""## 统计

- 知识点数量：{total}
- 已完成：{done}/{total} ({done/total*100:.0f}% if total else 0%)
"""

    moc_path = vault_path / domain / f"_{domain_name}_MOC.md"
    moc_path.write_text(content, encoding="utf-8")
    return moc_path

def generate_root_moc(notes_by_domain, vault_path):
    """Generate root README.md MOC."""
    today = datetime.now().strftime("%Y-%m-%d")

    content = f"""# 知识库总览

> 更新时间：{today}

## 知识导图 (Map of Content)

"""
    total_notes = 0
    total_done = 0

    for domain in sorted(notes_by_domain.keys()):
        if domain == "root":
            continue

        domain_notes = notes_by_domain[domain]
        domain_name = re.sub(r'^\d+-', '', domain)
        done = sum(1 for n in domain_notes if n["status"] == "final")
        total = len(domain_notes)
        total_notes += total
        total_done += done

        content += f"### [[{domain}/_{domain_name}_MOC|{domain_name}]] ({done}/{total})\n"
        # Show top 3 high-importance notes
        high = [n for n in domain_notes if n["importance"] == "high"][:3]
        for note in high:
            content += f"- [[{note['stem']}]]\n"
        if not high and domain_notes:
            for note in domain_notes[:2]:
                content += f"- [[{note['stem']}]]\n"
        content += "\n"

    content += f"""---

## 总体进度

- 知识点总数：{total_notes}
- 已完成：{total_done}/{total_notes}
- 完成率：{total_done/total_notes*100:.0f}%
"""

    readme_path = vault_path / "README.md"
    readme_path.write_text(content, encoding="utf-8")
    return readme_path

def main():
    vault_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    print(f"Scanning vault: {vault_path}")
    notes = scan_vault(vault_path)

    print(f"Found {sum(len(v) for v in notes.values())} notes in {len(notes)} domains")

    # Generate domain MOCs
    for domain, domain_notes in notes.items():
        if domain == "root":
            continue
        moc = generate_domain_moc(domain, domain_notes, vault_path)
        print(f"  Generated: {moc.relative_to(vault_path)}")

    # Generate root MOC
    root = generate_root_moc(notes, vault_path)
    print(f"  Generated: {root.relative_to(vault_path)}")

    print("\nMOC generation complete!")

if __name__ == "__main__":
    main()
