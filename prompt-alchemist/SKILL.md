# Prompt-Alchemist (提示词炼金术)

This skill acts as a "Prompt Firewall" and optimizer. It intercepts vague or low-quality user requests and transforms them into high-performance prompts before execution.

## Usage
- "I want to do X, but I don't know how to ask it well."
- "Refine my prompt for building a login page."
- [Triggered Automatically] "I detected your request might be too vague. Here is an optimized version..."

## Instructions
1. **Intercept & Analyze**: If a user's request is short (< 10 words) or lacks context (no clear goal, constraints, or format), trigger this skill.
2. **Optimize**: Rewrite the prompt using the "CO-STAR" or "Context-Task-Constraint" framework.
   - **Context**: Why are we doing this?
   - **Task**: What exactly needs to be done?
   - **Constraints**: What are the limits?
   - **Output**: What format is expected?
3. **Interactive Refinement**: Present the optimized prompt to the user as a block.
4. **Action**: Ask: "Does this look better? You can modify it or say 'GO' to proceed with this version."
5. **Iteration**: If the user modifies it, refine it again until they are satisfied.
