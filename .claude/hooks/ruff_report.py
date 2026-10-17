"""PostToolUse hook: report ruff problems in a Python file right after Claude edits it.

It only reports. It never fixes anything, so mistakes stay visible for learning.
Exit code 2 sends our stderr to Claude; exit code 0 means the file is clean.
"""

import json  # parse the JSON that Claude Code sends on stdin
import subprocess  # run another program and capture its output (Java: ProcessBuilder)
import sys  # stdin, stderr, exit codes, and the path of the running Python
from pathlib import Path  # file paths as objects (Java: java.nio.file.Path)


def ruff_problems(file_path: str) -> str:
    """Run ruff check and ruff format --check on one file; return the output, or ''."""
    reports = []  # an empty list we fill with text, like new ArrayList<String>()
    # Two checks: the linter finds bugs and style problems, the formatter checks layout.
    for arguments in (["check", file_path], ["format", "--check", file_path]):
        # sys.executable is the Python running this script, so we use the project's .venv.
        result = subprocess.run(
            [sys.executable, "-m", "ruff", *arguments],
            capture_output=True,  # keep the output instead of printing it
            text=True,  # decode bytes to str
            check=False,  # a non-zero exit is expected when ruff finds problems
        )
        if result.returncode != 0:
            reports.append(
                f"$ python -m ruff {' '.join(arguments)}\n{result.stdout}{result.stderr}"
            )
    return "\n".join(reports)


def main() -> int:
    """Read the hook input, check the edited file, and return the exit code."""
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0  # nothing useful to check, and this hook must never get in the way

    tool_input = payload.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    # Only look at Python files that still exist (the edit might have been a delete).
    if not file_path.endswith(".py") or not Path(file_path).is_file():
        return 0

    problems = ruff_problems(file_path)
    if problems:
        print(
            f"ruff found problems in {file_path} (report only, nothing was changed):",
            file=sys.stderr,
        )
        print(problems, file=sys.stderr)
        return 2  # PostToolUse: the edit already happened; stderr is shown to Claude
    return 0


# Runs main() only when executed directly (Java: public static void main).
if __name__ == "__main__":
    sys.exit(main())
