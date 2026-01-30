# Skill-Creator

A meta-skill that allows Claude to generate and install new custom skills for the user.

## Usage
- "I need a skill to help me organize my cooking recipes."
- "Create a skill for tracking my gym progress in Markdown."
- "Help me build a specialized skill for analyzing log files."

## Instructions
1. Gather requirements from the user about the desired automation.
2. Design a `SKILL.md` following the 2026 Progressive Disclosure pattern.
3. Automatically create the necessary directory in `~/.claude/skills/` and write the file.
