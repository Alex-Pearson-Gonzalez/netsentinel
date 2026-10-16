# Learning log

Newest first. One entry per concept or session, in my own words. `/teach` and `/wrap-up` draft entries for me to correct before they're saved.

## Template

```markdown
## YYYY-MM-DD · <concept>
- In my own words:
- Example I worked through:
- What I got wrong or found confusing:
- Still open:
- Resources:
```
## 2026-10-16 · pyproject.toml, pytest, ruff and Docker Compose
- In my own words: created a package where all the python files are, run and installed pytest by checking which version netsentinel is, ruff check is for finding likely bugs or mistakes before running the code and ruff format for fixing things like spacex, quotes... and created a docker compose service for the database we'll be using. 
- Example I worked through: installed pytest (the test runner) and wrote a smoke test that checks the package version.
- What I got wrong or found confusing: 
    ·had to run the command : python -m pip install -e ".[dev]", because Python couldn’t find the src/ folder until I installed the package with pip install -e, 
    ·I need to run the files with python -m pytest, 
    ·I also got wrong how to test something so that pytest can identify whats a test, the name of the function must have test_ before the name.
- Still open: what exactly a Docker named volume is and where the data lives, why -e (editable) instead of a normal insta
- Resources:https://docs.pytest.org, https://docs.astral.sh/ruff/, https://docs.docker.com/compose/ 

## 2026-10-13 · Virtual environments and PATH
- In my own words: it´s a virtual environment, where all the Python packages are so that they dont clash with other projects or folders
- Example I worked through: python -m venv .venv, activate, sys.prefix pointed into .venv
- What I got wrong or found confusing: python --version worked but python -m venv failed; the Windows Store alias came first in PATH
- Still open: why --version still worked through the alias
- Resources: https://docs.python.org/3/library/venv.html
