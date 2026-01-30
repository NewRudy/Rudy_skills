# Git Commit Helper

This skill helps the user create professional git commit messages by analyzing the staged changes.

## Usage
When the user wants to commit changes, use this skill to:
1. Run `git diff --cached` to see what's being committed.
2. Generate a concise, meaningful commit message following the project's style (or Conventional Commits).
3. Present the message to the user for approval.

## Prompt
"Analyze my staged changes and suggest a professional git commit message. Use the following format:
<type>(<scope>): <subject>

<body>"
