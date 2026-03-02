# Build Tools Reference

## Overview

Knowledge base products need export tools to generate study materials in Word/PDF format. All tools use Python + `python-docx`.

## Core Tools

### 1. build_document.py

Scans the knowledge base folders and compiles all notes into a single formatted Word document.

```python
# Usage: python tools/build_document.py
# Output: FINAL_PACKAGE/{vault_name}_完整手册.docx

# Key logic:
# 1. Walk numbered folders (01-*, 02-*, ...) in order
# 2. Read each .md file
# 3. Parse markdown headings → Word heading styles
# 4. Preserve bold, lists, tables
# 5. Add page breaks between sections
```

**Implementation notes**:
- Always use `encoding='utf-8'` for file I/O
- Handle Chinese characters in filenames
- Skip hidden files and tool directories
- Sort files by folder number prefix

### 2. build_guide.py

Generates a condensed study guide with only high-importance notes.

```python
# Usage: python tools/build_guide.py
# Output: FINAL_PACKAGE/{vault_name}_考点精华.docx

# Key logic:
# 1. Filter notes where frontmatter importance == "high"
# 2. Extract only "核心概念" and "要点总结" sections
# 3. Compile into compact format
```

### 3. create_word_doc.py

Generic markdown-to-Word converter for individual files.

```python
# Usage: python tools/create_word_doc.py <input.md> <output.docx>
# Supports: headings, bold, italic, lists, tables, blockquotes
```

### 4. generate_moc.py (MOC Generator)

Auto-generates Map of Content index files.

```python
# Usage: python tools/generate_moc.py
# Output: Updates README.md and per-folder MOC files

# Key logic:
# 1. Scan all .md files in vault
# 2. Extract frontmatter (title, domain, tags)
# 3. Group by folder/domain
# 4. Generate wikilink-based index
# 5. Calculate completion stats
```

## Setup

### Dependencies

```
pip install python-docx pyyaml
```

### CLAUDE.md Template

Every knowledge base vault should include a CLAUDE.md with:

```markdown
# CLAUDE.md

## Overview
{Brief description of the knowledge base and its purpose}

## Common Commands
### Document Generation
- **Build Full Handbook**: `python tools/build_document.py`
- **Build Study Guide**: `python tools/build_guide.py`

### Data Processing
- **Generate MOC Index**: `python tools/generate_moc.py`

## Architecture
- **`{NN}-{domain}/`**: Knowledge domain folders with structured MD content
- **`tools/`**: Build and export scripts using python-docx
- **`FINAL_PACKAGE/`**: Output directory for generated documents

## Development Guidelines
- **Encoding**: Always use `utf-8` for file I/O
- **Path Handling**: Use relative paths from vault root
- **File Format**: Markdown with YAML frontmatter
- **Dependencies**: python-docx, pyyaml
```

## Common Pitfalls

1. **Encoding**: Windows console uses GBK - avoid emoji/special chars in print statements
2. **Paths**: Use `pathlib.Path` for cross-platform compatibility
3. **Large files**: Some government docs are 50k+ chars - handle memory appropriately
4. **Frontmatter parsing**: Use `pyyaml` and handle files without frontmatter gracefully
