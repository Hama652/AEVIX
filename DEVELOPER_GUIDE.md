# Developer Guide

## Local Setup

1. Create a Python 3.12 environment.
2. Install the project in editable mode with development dependencies.
3. Run the validation script and the unit test suite before opening a review.

## Validation Commands

- `python scripts/validate_project.py`
- `pytest`
- `ruff check src tests scripts`
- `black --check src tests scripts`
- `mypy src`

## Working Rules

- Keep changes narrow and layered.
- Prefer extending shared infrastructure instead of duplicating logic in research code.
- Add config, docs, and tests together when they represent the same change.
