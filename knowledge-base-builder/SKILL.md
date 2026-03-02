---
name: knowledge-base-builder
description: >
  Automate creation, structuring, and management of Obsidian-based knowledge base products
  for exam preparation or any structured learning domain.
  Use when user wants to: (1) Create a new knowledge base / vault for an exam or topic,
  (2) Design directory structure for a knowledge base product,
  (3) Generate MOC (Map of Content) indexes,
  (4) Standardize note templates with frontmatter/tags/wikilinks,
  (5) Set up build tools for exporting to Word/PDF,
  (6) Plan content acquisition strategy for a knowledge base.
  Domains include but not limited to: 遴选, 软考, 公务员考试, CPA, PMP, 法考, or any exam/certification.
---

# Knowledge Base Builder

Build production-grade Obsidian knowledge base products for exam preparation and structured learning.

## Core Workflow

### Phase 1: Requirements Gathering

Ask the user:
1. **Exam/Domain**: What exam or knowledge domain? (e.g., 软考高项, 遴选, PMP)
2. **Scope**: What are the major knowledge areas / exam modules?
3. **Content sources**: Textbooks, official docs, online resources, past papers?
4. **Output needs**: Just Obsidian vault? Or also export to Word/PDF?
5. **Language**: Chinese / English / bilingual?

### Phase 2: Directory Structure Generation

Run `scripts/generate_structure.py` with the exam config to create the vault skeleton.

**Universal layered architecture** (proven pattern from 遴选知识库):

```
{vault_name}/
├── 00-考试大纲/           # Exam syllabus & overview
├── 01-{domain_1}/         # Knowledge domain folders (numbered)
│   ├── {subtopic_1}.md
│   └── {subtopic_2}.md
├── 02-{domain_2}/
├── ...
├── {N-3}-答题框架/        # Answer frameworks & templates
├── {N-2}-真题解析/        # Past exam analysis
├── {N-1}-时政动态/        # Current affairs (if applicable)
│   └── 官方原文/          # Original documents
├── {N}-模拟练习/          # Practice & mock exams
├── tools/                 # Build scripts
├── FINAL_PACKAGE/         # Export output directory
├── CLAUDE.md              # AI assistant instructions
└── README.md              # Vault overview & usage guide
```

**Naming conventions**:
- Folders: `{NN}-{中文名称}/` (numbered for sort order)
- Files: `{描述性名称}.md` (no dates unless time-sensitive)
- Time-sensitive files: `{名称}_{YYYYMMDD}.md`

### Phase 3: Note Templates

Generate standardized templates. See `references/templates.md` for all template types.

**Core template (every note)**:
```markdown
---
title: "{title}"
domain: "{knowledge_domain}"
tags: [{tag1}, {tag2}]
importance: {high|medium|low}
exam_frequency: {high|medium|low|unknown}
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
status: {draft|review|final}
---

# {title}

## 核心概念

## 要点总结

## 考点分析

> **考试提示**：{exam_tip}

## 关联知识
- [[related_note_1]]
- [[related_note_2]]
```

### Phase 4: MOC Generation

Run `scripts/generate_moc.py` to create Map of Content index files.

**MOC structure**:
- One MOC per top-level domain folder
- Root MOC (`README.md`) linking all domain MOCs
- Auto-updated when notes are added/modified

### Phase 5: Content Acquisition Strategy

Based on lessons learned, classify content sources:

| Source Type | Acquisition Method | Automation Level |
|------------|-------------------|-----------------|
| Textbook content | Manual OCR/typing → MD | Manual |
| Official standards/laws | Gov website direct URL | Semi-auto (Playwright) |
| Past exam papers | Manual collection → MD | Manual |
| Current affairs | AI-generated summaries | Auto (WebSearch → MD) |
| Framework/templates | AI-generated | Auto |

**Critical rule**: Verify every URL before adding to any index file. Never fabricate URLs.

### Phase 6: Build Tools Setup

Generate `tools/` scripts for the vault. See `references/build-tools.md` for details.

Core tools:
- `build_document.py` - Export knowledge base to Word
- `build_guide.py` - Generate study guide
- `create_word_doc.py` - Create formatted Word documents

## Key Lessons (from 遴选知识库)

1. **Content quality > content quantity** - 19 well-structured summary files > 100 raw documents
2. **Don't fabricate data** - Never create unverified URLs or fake content
3. **Structure first, content second** - Design the vault architecture before filling it
4. **Summaries > originals** - AI-generated structured summaries have higher study value than raw source texts
5. **80/20 rule** - Spend 80% effort on content quality and structure, 20% on tooling
6. **Verify before commit** - All data (URLs, facts, dates) must be verified before entering the knowledge base
7. **Incremental building** - Ship a usable v1 fast, iterate and expand over time
