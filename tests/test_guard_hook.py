"""Unit tests for the guard hook in .claude/hooks/guard.py."""

import importlib.util  # load a Python file by its path, because .claude is not a package
from pathlib import Path

import pytest  # the test framework; parametrize runs one test body for many inputs

# Build the path to the hook relative to this test file, so it works from any folder.
HOOK_PATH = Path(__file__).resolve().parents[1] / ".claude" / "hooks" / "guard.py"
spec = importlib.util.spec_from_file_location("guard", HOOK_PATH)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (".env", True),
        (".env.local", True),
        ("C:\\Users\\alexp\\dev\\netsentinel\\.env", True),  # Windows-style path
        ("./.ENV", True),  # Windows file names are not case sensitive
        (".env.example", False),  # the safe template is allowed
        ("src/netsentinel/env.py", False),
        ("docs/progress.md", False),
    ],
)
def test_is_blocked_path(path: str, expected: bool) -> None:
    assert guard.is_blocked_path(path) is expected


@pytest.mark.parametrize(
    ("command", "expected"),
    [
        ("git add .env", True),
        ("git add -f data/x.mrt", True),
        ("git add --force .", True),  # force can stage ignored files
        ("git add data/", True),
        ("git add dump.bz2 README.md", True),
        ("cd x && git add .env", True),  # hidden after another command
        ("git add src/netsentinel/cli.py", False),
        ("git add .env.example", False),
        ("git add .", False),  # .gitignore already protects us here
        ("git status", False),
        ("python -m pytest", False),
    ],
)
def test_is_blocked_command(command: str, expected: bool) -> None:
    assert guard.is_blocked_command(command) is expected
