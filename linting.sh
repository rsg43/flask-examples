#!/bin/bash

PY_FILES=$(git ls-files '*.py')

echo "Running linting checks:"

echo "Running black..."
python3 -m black $PY_FILES --line-length=79 --extend-exclude="data"

echo "Running flake8..."
python3 -m flake8 $PY_FILES --exclude="data"

echo "Running pylint..."
python3 -m pylint $PY_FILES --recursive=y --ignore-paths="^data/.*$"

echo "Running mypy..."
python3 -m mypy $PY_FILES --strict --exclude="data"

echo "Running pydoclint..."
pydoclint --style=sphinx --check-class-attributes=False --skip-checking-short-docstrings=False $PY_FILES

echo "Running semgrep..."
semgrep scan --error --config auto

echo "Linting checks complete."
