# Planning-with-Files

This skill enhances Claude's long-term memory and project consistency by using local Markdown files as an external state/context store.

## Usage
- "Initialize a new project plan using files."
- "Update the task status in our project plan."
- "Review our current progress based on the notes file."

## Instructions
1. Maintain three core files in the project root: `task_plan.md` (roadmap), `context_log.md` (decision history), and `status.md` (current state).
2. Before starting any major task, read these files to ensure alignment.
3. After completing a task, update the files to prevent "context drift" in future sessions.
4. Use clear markers (e.g., [TODO], [DONE], [BLOCKED]) to make the status machine-readable.
