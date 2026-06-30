# Contributing to AEVIX

AEVIX contributions should preserve long-term maintainability, strong typing, and clear architectural boundaries.

## Expectations

- Prefer small, reviewable changes.
- Add or update tests for behavior changes.
- Keep public APIs stable unless the change is explicitly architectural.
- Follow the coding standards in `CODING_STANDARDS.md`.

## Workflow

1. Read the relevant architecture and standards documents before editing.
2. Run the narrowest useful validation locally.
3. Keep changes focused on one responsibility at a time.
4. Avoid introducing cross-layer imports or hidden dependencies.

## Review Criteria

- Does the change improve the repository foundation rather than just solving a local symptom?
- Is the code fully typed and covered by tests where practical?
- Are configuration, logging, and file-system interactions explicit and deterministic?
