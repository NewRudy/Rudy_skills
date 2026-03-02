"""
Office-to-Markdown Cleanup Script v2
Fixes Pandoc conversion artifacts for Obsidian compatibility.
Handles fuzzy TOC-to-heading matching.
"""
import re
import sys

def cleanup_md(input_path, output_path=None):
    if output_path is None:
        output_path = input_path

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # ============================================
    # Phase 1: Clean Word/Pandoc artifacts FIRST
    # ============================================

    # 1a. Clean TOC anchor links: [title [page](#_TocXXX)](#_TocXXX) -> [[#title]]
    text = re.sub(r'\[([^\[\]]+?)\s*\[\d+\]\(#_Toc\d+\)\]\(#_Toc\d+\)', r'[[#\1]]', text)
    text = re.sub(r'\[([^\[\]]+?)\s*\[\d+\]\(#heading_\d+\)\]\(#heading_\d+\)', r'[[#\1]]', text)

    # 1b. Clean []{#_TocXXX .anchor}
    text = re.sub(r'\[\]\{#_Toc\d+\s+\.anchor\}', '', text)
    text = re.sub(r'\[\]\{#heading_\d+\s+\.anchor\}', '', text)

    # 1c. Clean [text]{.mark} -> text, [text]{.underline} -> text
    text = re.sub(r'\[([^\[\]]*?)\]\{\.mark\}', r'\1', text)
    text = re.sub(r'\[([^\[\]]*?)\]\{\.underline\}', r'\1', text)

    # 1d. Clean remaining {.mark} {.underline} {.anchor}
    text = re.sub(r'\{\.mark\}', '', text)
    text = re.sub(r'\{\.underline\}', '', text)
    text = re.sub(r'\{\.anchor\}', '', text)

    # 1e. Clean image size attributes
    text = re.sub(r'\{width="[^"]*"\s*\n?\s*height="[^"]*"\}', '', text)
    text = re.sub(r'\{width="[^"]*"\}', '', text)
    text = re.sub(r'\{height="[^"]*"\}', '', text)

    # 1f. Clean <!-- -->
    text = re.sub(r'<!-- -->\n?', '', text)

    # 1g. Image paths to Obsidian format
    text = re.sub(r'!\[\]\(\./media/media/([^)]+)\)', r'![[media/media/\1]]', text)
    text = re.sub(r'!\[\]\(\.?/?media/([^)]+)\)', r'![[media/\1]]', text)

    # ============================================
    # Phase 2: Fix TOC -> Heading matching
    # ============================================
    lines = text.split('\n')

    # 2a. Find TOC region (consecutive lines with [[#...]])
    toc_entries = []
    toc_end_idx = 0
    for i, line in enumerate(lines):
        m = re.search(r'\[\[#(.+?)\]\]', line)
        if m:
            toc_entries.append(m.group(1))
            toc_end_idx = i

    def get_heading_level(entry):
        if re.match(r'^[一二三四五六七八九十]+、', entry):
            return 1
        if re.match(r'^\d+\.\d+\.\d+', entry):
            return 4
        if re.match(r'^\d+\.\d+', entry):
            return 3
        if re.match(r'^\d+[\.\s]', entry):
            return 2
        return 2

    def extract_core(text_str):
        """Extract core content by removing numbering and common suffixes."""
        s = text_str.strip()
        s = re.sub(r'^[一二三四五六七八九十]+、\s*', '', s)
        s = re.sub(r'^\d+[\.\s]+', '', s)
        s = re.sub(r'^\d+\.\d+[\.\s]*', '', s)
        s = re.sub(r'[（(][^）)]*[）)]$', '', s)
        s = re.sub(r'~~.*?~~', '', s)
        return s.strip()

    # 2c. For each TOC entry, find best matching body line
    matched = set()
    for entry in toc_entries:
        level = get_heading_level(entry)
        hashes = '#' * level
        core = extract_core(entry)
        if not core or len(core) < 2:
            continue

        best_idx = -1
        best_score = 0
        for i in range(toc_end_idx + 1, len(lines)):
            if i in matched:
                continue
            line = lines[i].strip()
            if not line or line.startswith('#') or len(line) > 300:
                continue
            if line.count('\u3002') > 2:
                continue

            line_core = extract_core(line)
            if not line_core:
                continue

            if core == line_core:
                best_idx = i
                best_score = 100
                break
            if core in line_core and len(core) >= 3:
                score = len(core) / len(line_core) * 80
                if score > best_score:
                    best_score = score
                    best_idx = i
            if line_core in core and len(line_core) >= 3:
                score = len(line_core) / len(core) * 70
                if score > best_score:
                    best_score = score
                    best_idx = i

        if best_idx >= 0 and best_score >= 40:
            old_line = lines[best_idx].strip()
            cleaned = re.sub(r'^\d+\.\s{2,}', '', old_line)
            lines[best_idx] = hashes + ' ' + cleaned
            matched.add(best_idx)

    text = '\n'.join(lines)

    # ============================================
    # Phase 3: Final cleanup
    # ============================================
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    return len(matched), len(toc_entries)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python cleanup_md.py <input.md> [output.md]')
        sys.exit(1)
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else inp
    matched, total = cleanup_md(inp, out)
    print('Done: matched %d/%d TOC entries to headings' % (matched, total))
