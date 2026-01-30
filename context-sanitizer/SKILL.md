# Context-Sanitizer (安全与隐私哨兵)

Ensures that no sensitive data is leaked during tool execution, code generation, or git operations.

## Usage
- "Scan my current staged changes for secrets."
- "Is it safe to run this bash command?"
- [Automatic] "Hold on, I detected a potential API key in your request. Should I mask it?"

## Instructions
1. **Secret Detection**: Scan for patterns matching API keys, passwords, private keys, and PII (Personally Identifiable Information).
2. **Risk Assessment**: Evaluate the danger of proposed Bash commands (e.g., destructive `rm` or network requests to unknown IPs).
3. **Masking**: Automatically offer to mask or redact sensitive strings before they are processed by the LLM or external tools.
4. **Permission Gate**: Always ask for confirmation before executing high-risk operations.
