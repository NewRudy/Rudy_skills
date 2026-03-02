# html2word Skill - Core Prompt Template

You are generating a Word-compatible HTML file with perfect formatting preservation.

## Critical HTML Rules (MUST FOLLOW)

1. **Inline Styles Only**: All styling MUST be in `style=""` attributes. NEVER use `<style>` tags or external CSS.
2. **Use `pt` (points) for font sizes**: NEVER use `px` (pixels). Common sizes:
   - 3号 (三号) = 16pt
   - 小三 = 15pt
   - 4号 (四号) = 14pt
   - 小四 = 12pt
   - 5号 (五号) = 10.5pt
3. **Table centering**: Use `align="center"` attribute on `<table>` tag, NOT CSS `margin: auto`.
4. **Body margins**: Set `<body style="margin: 0; padding: 0;">` to prevent page offset.
5. **Character encoding**: ALWAYS include `<meta charset="UTF-8">` in `<head>`.
6. **First-line indent**: Use `text-indent: 24pt` for 2-character indent (Chinese standard).

## Font Size Reference

| 中文名称 | 英文 | pt大小 | 用途 |
|---------|------|--------|------|
| 三号 | Size 3 | 16pt | 主标题 |
| 小三 | Small 3 | 15pt | 一级标题 |
| 四号 | Size 4 | 14pt | 二级标题 |
| 小四 | Small 4 | 12pt | 正文 |
| 五号 | Size 5 | 10.5pt | 注释/脚注 |

## Mathematical Formula Handling

### For LaTeX formulas:

**Inline formula** (行内公式): Use single `$...$`
```
质能方程 $E=mc^2$ 和圆面积 $A=π r^2$
```

**Display formula** (独立公式): Use double `$$...$$` with centered gray background
```html
<p style="text-align: center; background-color: #f5f5f5; padding: 8pt; margin: 12pt 0;">
$$x = \frac{-b ± \sqrt{b^2-4ac}}{2a}$$
</p>
```

**Greek Letters**: Use Unicode characters directly instead of LaTeX commands:
- π (not \pi)
- α (not \alpha)
- σ (not \sigma)
- Δ (not \Delta)
- ± (not \pm)

### VBA Macro for Formula Conversion

When formulas are present, embed the VBA macro code in HTML comments at the beginning of the file.

## Multi-Level Lists

Use `margin-left` to control indentation levels:
- Level 1: `margin-left: 24pt`
- Level 2: `margin-left: 48pt`
- Level 3: `margin-left: 72pt`
- Level 4: `margin-left: 96pt`

```html
<p style="margin-left: 24pt; line-height: 1.5;">• Level 1 item</p>
<p style="margin-left: 48pt; line-height: 1.5;">• Level 2 item</p>
```

## Images

### Base64 Embedded Images:
```html
<p style="text-align: center;">
  <img src="data:image/png;base64,..." style="width: 300pt; height: auto;">
</p>
```

### Local Image References:
```html
<img src="path/to/image.png" style="width: 300pt; height: auto; border: 1pt solid #ddd;">
```

## Standard Document Template

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Document Title</title>
</head>
<body style="margin: 0; padding: 0; font-family: 宋体;">

<!-- Title -->
<p style="font-family: 宋体; font-size: 16pt; font-weight: bold; text-align: center; margin: 12pt 0;">
    文档标题
</p>

<!-- Level 1 Heading -->
<p style="font-family: 宋体; font-size: 15pt; font-weight: bold; margin: 12pt 0 6pt 0;">
    一、一级标题
</p>

<!-- Body Paragraph -->
<p style="font-family: 宋体; font-size: 12pt; text-indent: 24pt; line-height: 1.5; margin: 6pt 0;">
    正文内容，首行缩进两个字符。
</p>

<!-- Level 2 Heading -->
<p style="font-family: 宋体; font-size: 14pt; font-weight: bold; margin: 10pt 0 6pt 0;">
    1.1 二级标题
</p>

<!-- Table (centered) -->
<table align="center" style="width: auto; border-collapse: collapse; font-family: 宋体; font-size: 12pt; margin: 12pt auto;">
    <tr>
        <th style="border: 1pt solid black; padding: 6pt; background-color: #f0f0f0;">表头</th>
    </tr>
    <tr>
        <td style="border: 1pt solid black; padding: 6pt;">内容</td>
    </tr>
</table>

</body>
</html>
```

## Output Instructions

1. Generate complete HTML file with all inline styles
2. If formulas are present, include VBA macro in HTML comments
3. Ensure all Chinese characters display correctly (UTF-8 encoding)
4. Test that tables are centered with `align="center"`
5. Verify font sizes are in `pt` units

## User Workflow After Generation

1. Open HTML in browser to preview
2. Press Ctrl+A to select all, Ctrl+C to copy
3. Paste into Word with "Keep Source Formatting"
4. If formulas present: Alt+F11 → Insert Module → Run VBA macro
5. Manually add headers/footers in Word if needed
