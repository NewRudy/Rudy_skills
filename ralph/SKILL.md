# Ralph (Autonomous Coding Loop)

Equips Claude with an autonomous feedback loop to self-correct and iterate until a task is fully resolved.

## Usage
- "Use Ralph to refactor this module until all tests pass."
- "Implement this feature autonomously, fixing any errors that arise."
- "Start a Ralph loop for this bug fix."

## Instructions
1. **Iterative Cycle**: Execute code -> Catch error -> Analyze root cause -> Fix code -> Repeat.
2. **Termination**: Only stop once the goal is achieved (e.g., tests pass) or a hard limit is reached.
3. **Transparency**: Report each iteration's progress and findings to the user.
