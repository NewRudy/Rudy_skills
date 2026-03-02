#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knowledge Base Structure Generator
Generates an Obsidian vault directory structure based on exam configuration.
Usage: python generate_structure.py --config config.json --output ./output_vault
"""

import json
import sys
from pathlib import Path
from datetime import datetime

DEFAULT_CONFIGS = {
    "软考高项": {
        "vault_name": "软考高项知识库",
        "domains": [
            {"id": "01", "name": "信息系统综合知识", "subtopics": [
                "信息系统概述", "信息技术发展", "信息系统开发方法",
                "系统规划", "系统分析", "系统设计", "系统实施",
                "系统运维", "新一代信息技术"
            ]},
            {"id": "02", "name": "项目管理知识体系", "subtopics": [
                "项目管理概论", "项目整合管理", "项目范围管理",
                "项目进度管理", "项目成本管理", "项目质量管理",
                "项目资源管理", "项目沟通管理", "项目风险管理",
                "项目采购管理", "项目干系人管理"
            ]},
            {"id": "03", "name": "高级项目管理", "subtopics": [
                "项目集管理", "项目组合管理", "组织级项目管理",
                "量化项目管理", "项目管理成熟度模型"
            ]},
            {"id": "04", "name": "信息化与信息安全", "subtopics": [
                "信息化发展与应用", "电子政务", "企业信息化",
                "信息安全基础", "信息安全管理体系", "信息安全等级保护"
            ]},
            {"id": "05", "name": "法律法规与标准", "subtopics": [
                "知识产权", "招投标法", "政府采购法",
                "合同法相关", "信息安全相关法规", "标准化知识"
            ]},
            {"id": "06", "name": "案例分析", "subtopics": [
                "案例分析方法论", "项目管理案例", "信息系统案例",
                "综合分析案例"
            ]},
            {"id": "07", "name": "论文写作", "subtopics": [
                "论文写作方法", "论文模板", "高分论文范例",
                "论文素材库"
            ]},
            {"id": "08", "name": "真题解析", "subtopics": []},
            {"id": "09", "name": "模拟练习", "subtopics": []},
        ],
        "has_current_affairs": False,
    },
    "遴选": {
        "vault_name": "遴选知识库",
        "domains": [
            {"id": "01", "name": "政治理论", "subtopics": [
                "习近平新时代中国特色社会主义思想",
                "党的二十大精神", "全面从严治党"
            ]},
            {"id": "02", "name": "省情市情", "subtopics": []},
            {"id": "03", "name": "公文写作", "subtopics": []},
            {"id": "04", "name": "答题框架", "subtopics": []},
            {"id": "05", "name": "案例分析", "subtopics": []},
            {"id": "06", "name": "时政动态", "subtopics": [
                "中央重大会议", "重要政策文件", "官方原文"
            ]},
            {"id": "07", "name": "真题解析", "subtopics": []},
            {"id": "08", "name": "模拟练习", "subtopics": []},
        ],
        "has_current_affairs": True,
    },
}

def generate_vault(config, output_path):
    """Generate vault directory structure from config."""
    vault_path = Path(output_path) / config["vault_name"]
    vault_path.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    created_files = []

    # Create domain folders and subtopic files
    for domain in config["domains"]:
        domain_path = vault_path / f"{domain['id']}-{domain['name']}"
        domain_path.mkdir(exist_ok=True)

        # Create MOC for each domain
        moc_content = f"""---
title: "{domain['name']} - 知识导图"
type: moc
tags: [MOC, 索引]
updated: {today}
---

# {domain['name']} - 知识导图

## 知识结构

"""
        for subtopic in domain.get("subtopics", []):
            # Create subtopic file
            note_path = domain_path / f"{subtopic}.md"
            note_content = f"""---
title: "{subtopic}"
domain: "{domain['name']}"
tags: [{domain['name']}]
importance: medium
exam_frequency: unknown
created: {today}
updated: {today}
status: draft
---

# {subtopic}

## 核心概念



## 要点总结

1.

## 考点分析

> **考试提示**：

## 关联知识

- [[]]
"""
            note_path.write_text(note_content, encoding="utf-8")
            created_files.append(str(note_path.relative_to(vault_path)))
            moc_content += f"- [[{subtopic}]]\n"

        # Write MOC
        moc_path = domain_path / f"_{domain['name']}_MOC.md"
        moc_path.write_text(moc_content, encoding="utf-8")
        created_files.append(str(moc_path.relative_to(vault_path)))

    # Create tools directory
    tools_path = vault_path / "tools"
    tools_path.mkdir(exist_ok=True)

    # Create output directory
    (vault_path / "FINAL_PACKAGE").mkdir(exist_ok=True)

    # Create CLAUDE.md
    claude_md = f"""# CLAUDE.md

## Overview
{config['vault_name']} - Obsidian-based knowledge base for exam preparation.

## Common Commands
### Document Generation
- **Build Full Handbook**: `python tools/build_document.py`
- **Build Study Guide**: `python tools/build_guide.py`

## Architecture
{chr(10).join(f"- **`{d['id']}-{d['name']}/`**: {d['name']} knowledge domain" for d in config['domains'])}
- **`tools/`**: Build and export scripts
- **`FINAL_PACKAGE/`**: Output directory

## Development Guidelines
- **Encoding**: Always use `utf-8` for file I/O
- **File Format**: Markdown with YAML frontmatter
- **Dependencies**: python-docx, pyyaml
"""
    (vault_path / "CLAUDE.md").write_text(claude_md, encoding="utf-8")
    created_files.append("CLAUDE.md")

    # Create README.md (root MOC)
    readme = f"""# {config['vault_name']}

> Created: {today}

## 知识导图 (Map of Content)

"""
    for domain in config["domains"]:
        readme += f"### [[{domain['id']}-{domain['name']}/_{domain['name']}_MOC|{domain['name']}]]\n"
        for st in domain.get("subtopics", [])[:3]:
            readme += f"- [[{st}]]\n"
        if len(domain.get("subtopics", [])) > 3:
            readme += f"- ... ({len(domain['subtopics'])} topics)\n"
        readme += "\n"

    (vault_path / "README.md").write_text(readme, encoding="utf-8")
    created_files.append("README.md")

    return vault_path, created_files

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_structure.py <exam_type> [output_path]")
        print(f"\nAvailable types: {', '.join(DEFAULT_CONFIGS.keys())}")
        print("Or: python generate_structure.py --config config.json [output_path]")
        sys.exit(1)

    exam_type = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "."

    if exam_type == "--config":
        config_file = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else "."
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
    elif exam_type in DEFAULT_CONFIGS:
        config = DEFAULT_CONFIGS[exam_type]
    else:
        print(f"Unknown exam type: {exam_type}")
        print(f"Available: {', '.join(DEFAULT_CONFIGS.keys())}")
        sys.exit(1)

    vault_path, files = generate_vault(config, output_path)
    print(f"\nVault created: {vault_path}")
    print(f"Files generated: {len(files)}")
    for f in files:
        print(f"  {f}")

if __name__ == "__main__":
    main()
