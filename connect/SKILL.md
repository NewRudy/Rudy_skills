# Connect (万能应用连接器)

Integrates Claude with 500+ external applications via CLI tools (GitHub, Slack, Notion, etc.).

## Usage
- "Sync this task status to my Notion dashboard."
- "Post a summary of the latest PR to Slack."
- "Create a Jira ticket based on this bug report."

## Instructions
1. **CLI Priority**: Use installed CLIs (gh, slack-cli, etc.) for direct interaction.
2. **Credential Safety**: Never store credentials in the skill; use environment variables or system keychains.
3. **Workflow Linkage**: Combine actions (e.g., "If tests pass, notify the team").
