"""PreToolUse hook: stop Claude from touching secrets or staging data files.

Claude Code runs this script before every Edit, Write, Bash and PowerShell call.
It reads one JSON document on stdin. Exit code 2 blocks the call and sends
whatever we print on stderr back to Claude. Any other exit code lets it through.
"""

import json  # parse the JSON that Claude Code sends us (Java: Jackson / Gson)
import re  # regular expressions, used to split a shell command into parts
import sys  # stdin, stderr and exit codes (Java: System.in, System.err, System.exit)
from pathlib import PurePosixPath  # path maths on text only, never touches the disk

# Files that must never be staged with git, because they are secrets or big data dumps.
PROTECTED_SUFFIXES = (".mrt", ".bz2", ".gz")  # a tuple: like a fixed, unchangeable list
PROTECTED_DIRECTORY = "data"


def normalise_path(path: str) -> str:
    """Turn a Windows-style path into a lowercase path with forward slashes."""
    # Windows paths use backslashes; we convert so one set of rules works everywhere.
    cleaned = path.strip().strip("\"'").replace("\\", "/").lower()
    # "./data/x" and "data/x" mean the same thing, so drop a leading "./".
    return cleaned.removeprefix("./")


def is_env_file(path: str) -> bool:
    """True for .env and .env.<anything>, but not for the safe template .env.example."""
    # PurePosixPath(...).name is the last part of the path (Java: Path.getFileName()).
    name = PurePosixPath(normalise_path(path)).name
    if name == ".env.example":
        return False
    return name == ".env" or name.startswith(".env.")


def is_blocked_path(path: str) -> bool:
    """True if Claude must not edit or write this file."""
    return is_env_file(path)


def is_protected_for_git(argument: str) -> bool:
    """True if a git argument names a secret or a data file we never commit."""
    path = normalise_path(argument)
    if is_env_file(path):
        return True
    if path.endswith(PROTECTED_SUFFIXES):  # endswith accepts a tuple of options
        return True
    # "data" itself, or anything inside data/
    return path == PROTECTED_DIRECTORY or path.startswith(PROTECTED_DIRECTORY + "/")


def is_blocked_command(command: str) -> bool:
    """True if a shell command stages protected files with git add."""
    # A single line can hold several commands: "cd x && git add .env". Split them apart.
    segments = re.split(r"&&|\|\||[;|\n]", command)
    for segment in segments:
        words = segment.split()  # split on whitespace, like Java's String.split("\\s+")
        if len(words) < 2 or words[0] != "git" or words[1] != "add":
            continue  # not a "git add" command, so ignore this segment
        arguments = words[2:]
        # --force stages files even if .gitignore ignores them. That is how secrets leak.
        if "-f" in arguments or "--force" in arguments:
            return True
        if any(is_protected_for_git(argument) for argument in arguments):
            return True
    return False


def main() -> int:
    """Read the hook input, decide, and return the exit code."""
    try:
        payload = json.load(sys.stdin)  # parse stdin into a dict (Java: Map<String, Object>)
    except json.JSONDecodeError:
        # If we cannot read the input, do not block everything. Exit 1 is a warning only.
        print("guard.py: could not read hook input; allowing the call.", file=sys.stderr)
        return 1

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {})

    if tool_name in ("Edit", "Write"):
        file_path = tool_input.get("file_path", "")
        if is_blocked_path(file_path):
            print(
                f"Blocked: {file_path} is an environment file. "
                "Secrets stay out of Claude's hands; edit it yourself. "
                "Use .env.example for variable names.",
                file=sys.stderr,
            )
            return 2  # 2 = block the tool call

    if tool_name in ("Bash", "PowerShell"):
        command = tool_input.get("command", "")
        if is_blocked_command(command):
            print(
                "Blocked: this git add would stage a secret, a data dump, or use --force. "
                "Ask the user first.",
                file=sys.stderr,
            )
            return 2

    return 0  # 0 = allow


# Runs main() only when the file is executed directly, not when a test imports it.
# Java equivalent: public static void main(String[] args).
if __name__ == "__main__":
    sys.exit(main())
