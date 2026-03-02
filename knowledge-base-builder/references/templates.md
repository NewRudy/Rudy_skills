# Note Templates Reference

## 1. Knowledge Point Template (知识点模板)

```markdown
---
title: "{title}"
domain: "{knowledge_domain}"
tags: []
importance: medium
exam_frequency: unknown
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
status: draft
---

# {title}

## 核心概念

{concept_description}

## 要点总结

1.
2.
3.

## 考点分析

> **考试提示**：

## 典型例题

## 关联知识

- [[]]
```

## 2. Framework Template (答题框架模板)

```markdown
---
title: "{framework_name}"
type: framework
domain: "{domain}"
tags: [框架, 答题模板]
created: {YYYY-MM-DD}
---

# {framework_name}

## 适用题型

-

## 答题结构

### 开头段（引题）

{opening_template}

### 主体段（分论点）

**分论点一**：
**分论点二**：
**分论点三**：

### 结尾段（总结升华）

{closing_template}

## 高频素材

| 关键词 | 可用表述 |
|-------|---------|
| | |

## 真题应用示例

- [[]]
```

## 3. Exam Paper Analysis Template (真题解析模板)

```markdown
---
title: "{year}年{exam_name}真题解析"
type: exam_paper
year: {year}
tags: [真题, {year}]
created: {YYYY-MM-DD}
---

# {year}年{exam_name}真题解析

## 考试概况

- **考试时间**：
- **题型分布**：
- **难度评估**：

## 题目解析

### 第一题

**题目**：

**参考答案**：

**考点分析**：涉及 [[]] 知识点

**评分标准**：

---

## 高频考点统计

| 考点 | 出现频率 | 关联知识 |
|------|---------|---------|
| | | [[]] |

## 命题趋势分析

```

## 4. Current Affairs Template (时政动态模板)

```markdown
---
title: "{event_name}"
type: current_affairs
date: {YYYY-MM-DD}
source: "{source}"
tags: [时政, {year}]
importance: medium
created: {YYYY-MM-DD}
---

# {event_name}

> **发布时间**：{date}
> **来源**：{source}

## 核心内容

## 考试关联

与以下知识点相关：
- [[]]

## 可能考法

1.
2.

## 原文链接

-
```

## 5. MOC Template (Map of Content 模板)

```markdown
---
title: "{domain_name} - 知识导图"
type: moc
tags: [MOC, 索引]
updated: {YYYY-MM-DD}
---

# {domain_name} - 知识导图

## 概述

{domain_description}

## 知识结构

### {subtopic_1}
- [[note_1]]
- [[note_2]]

### {subtopic_2}
- [[note_3]]
- [[note_4]]

## 学习路径

1. **入门**：先阅读 [[]]
2. **进阶**：掌握 [[]]
3. **冲刺**：练习 [[]]

## 统计

- 知识点数量：{count}
- 完成状态：{done}/{total}
```

## 6. Official Document Index Template (官方文件索引模板)

```markdown
---
title: "官方原文链接索引"
type: index
tags: [索引, 官方原文]
updated: {YYYY-MM-DD}
---

# 官方原文链接索引

> **更新日期**：{date}
> **验证状态**：所有链接需经过验证

## 文件列表

### {category_1}

#### {doc_name}

**完整标题**：《{full_title}》
**发布时间**：{date}
**官方来源**（需验证后标注✅）：
- {source_url}

**本地文件**：`{filename}.md` {status}
**核心要点**：[[{summary_note}]]

---

## 下载状态

- ✅ 已验证下载
- 📋 URL已验证待下载
- ❌ URL失效需重新查找

## 重要规则

1. **永远不要编造URL** - 所有链接必须通过WebSearch验证
2. **标注验证状态** - 每个URL都要标明是否验证过
3. **提供备用来源** - 每个文件至少2个官方来源
```
