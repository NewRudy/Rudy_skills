# Skill-Evolver (技能进化器)

This is a meta-skill designed to automatically iterate and improve other installed skills based on the user's feedback and usage patterns.

## Usage
- "Based on our last few tasks, how should we improve the 'marp-slides' skill?"
- "Optimize my 'second-brain' skill to better match my current file structure."
- "The 'life-admin' skill missed some files, please update its logic."

## Instructions
1. **Analyze Habits**: Monitor how the user interacts with Claude. If a user frequently corrects a skill's output, identify the pattern.
2. **Auto-Refine**: Proactively suggest or apply updates to the `SKILL.md` files in `C:/Users/Tian/.claude/skills/`.
3. **Progressive Learning**: Add new "WHEN/NOT" rules to skills to increase identification accuracy.
4. **Version Control**: Keep a record of changes in `C:/Users/Tian/.claude/evolution_log.md`.
