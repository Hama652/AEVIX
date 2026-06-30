# AEVIX

AEVIX is being built as a long-lived research and engineering platform for foundation models, scientific AI, cybersecurity AI, coding models, and future multimodal systems.

This repository currently contains the software foundation only. Model code, training loops, tokenizers, datasets, and distributed execution are intentionally out of scope for this phase.

## Current Phase

Phase 1 establishes the repository structure, shared infrastructure, and engineering standards that future model families will inherit.

Included in this phase:

- typed Python package scaffolding under `src/aevix`
- YAML-based configuration loading for development, testing, production, and future distributed training
- enterprise-oriented logging primitives for console and file output
- shared utilities for paths, filesystem operations, environment handling, serialization, seeding, timers, and checkpoint metadata
- registry, interface, exception, and base type layers for future components
- initial tests and automation hooks for quality gates

## Repository Principles

- Prefer clarity over cleverness.
- Keep dependencies explicit and minimal.
- Make all infrastructure code reusable by later research and production systems.
- Preserve strict typing, consistent formatting, and testability.

## Layout

- `.github/` CI and automation workflows
- `configs/` YAML configuration profiles
- `docs/` supporting documentation
- `research/` research-process guidance and future experiment notes
- `scripts/` utility scripts for local validation and maintenance
- `src/` installable Python package
- `tests/` unit and integration tests

## Development Snapshot

The package is designed for Python 3.12 with Black, Ruff, Pytest, and Mypy as the baseline engineering toolchain. PyTorch and CUDA are part of the future runtime plan, but they are not required for this foundation phase.

## Next Phase

After review, the next layer will add research-facing abstractions for experiment management, metric tracking, and stronger configuration validation while still avoiding model implementation.