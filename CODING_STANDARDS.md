# Coding Standards

## Language Standards

- Python 3.12 only for repository code.
- Use full type annotations for public functions, methods, and data structures.
- Prefer Google-style docstrings for public APIs.
- Follow PEP 8 and keep formatting compatible with Black.

## Architecture Standards

- Do not create circular imports.
- Avoid unnecessary abstractions.
- Keep files focused on a single responsibility.
- Prefer protocol and dataclass boundaries over ad hoc dictionaries when the shape is important.

## Quality Standards

- New behavior should be covered by tests.
- Keep error messages specific and actionable.
- Validate external inputs at the boundary of each subsystem.
- Do not log secrets or large binary payloads.
