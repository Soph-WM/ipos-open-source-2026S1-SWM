# this is an optional command runner using the "just" cli tool to make a starting server's
# and complex command easier

# more info on how to install here: https://github.com/casey/just#packages
# or run: `uv tool install rust-just`
# then run a recipe like 'just run' in your console

PYTHON := "uv run"
PIP := "uv pip"

# run the main script
run:
    {{ PYTHON }} main.py

# run the test suite
test:
    {{ PYTHON }} pytest -v

# format, lint and type check the code
check:
    {{ PYTHON }} ruff format . && {{ PYTHON }} ruff check .
    {{ PYTHON }} ty check .

# update dependencies
update-dependencies:
    {{ PIP }} compile pyproject.toml -o requirements.txt
    {{ PIP }} compile pyproject.toml --group dev -o requirements-dev.txt
