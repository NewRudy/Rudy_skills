# Office to Markdown Converter

## Overview
Converts Office documents (DOCX, PPTX, XLSX, PDF) to Obsidian-compatible Markdown using Pandoc and a Python cleanup script.

## Usage
- "Convert this docx to markdown"
- "Convert E:\Documents\report.docx to md"
- /office-to-md path/to/file.docx

## Prerequisites
- **Pandoc** (install via `winget install JohnMacFarlane.Pandoc`)
- **Python 3** with standard library

## Instructions

### Step 1: Identify the source file
- Accept file path from user (absolute or relative to vault)
- Supported formats: .docx, .pptx, .xlsx, .pdf

### Step 2: Determine output location
- Default: same directory as source, with `.md` extension
- Media files extracted to `./media/` subdirectory next to the output file
- Ask user if they want a different output location

### Step 3: Run Pandoc conversion
```bash
pandoc "<input_file>" -t markdown -o "<output_file>" --extract-media=./media
```

### Step 4: Run cleanup script
Run the cleanup script bundled with this skill:
```bash
python "C:\Users\Tian\.claude\skills\office-to-md\cleanup_md.py" "<output_file>"
```

### Step 5: Report results
Report to user:
- Output file path and size
- Number of images extracted
- Number of TOC entries matched to headings
- Any remaining issues to manually review

## What the cleanup script fixes

| Issue | Source | Fix |
|-------|--------|-----|
| `[title [page](#_TocXXX)](#_TocXXX)` | Word TOC bookmarks | Convert to `[[#title]]` Obsidian wikilinks |
| `[]{#_TocXXX .anchor}` | Word bookmark anchors | Remove |
| `[text]{.mark}` | Word highlight style | Keep text, remove markup |
| `[text]{.underline}` | Word underline style | Keep text, remove markup |
| `{width="..." height="..."}` | Word image dimensions | Remove |
| `<!-- -->` | Pandoc HTML separators | Remove |
| `![](./media/...)` | Standard markdown images | Convert to `![[media/...]]` |
| Missing `#` headings | Word heading styles not detected | Fuzzy-match TOC entries to body text and add `#` markers |

## Notes
- The TOC-to-heading matching uses fuzzy logic: it extracts the "core" text from both TOC entries and body lines (stripping numbering, annotations, etc.) and matches them. Match rate varies by document quality (typically 50-90%).
- For best results, use consistent Heading styles (Heading 1/2/3) in Word before converting.
- After conversion, manually review the output for any remaining formatting issues.
