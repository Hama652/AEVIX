# Architecture

AEVIX follows a clean, layered structure intended to stay stable as research code evolves into production systems.

## Layering

- `core`: shared component abstractions and base metadata
- `config`: profile loading, merge logic, and runtime configuration resolution
- `logging`: structured logging setup and logger configuration
- `interfaces`: protocol-style contracts for cross-layer behavior
- `exceptions`: repository-wide error hierarchy
- `types`: shared type aliases and primitive data definitions
- `utils`: filesystem, path, serialization, seeding, timer, and checkpoint helpers
- `registry`: explicit registry primitives for controlled extensibility
- `models`, `training`, `evaluation`, `tokenizer`: future-facing domain layers that currently expose only base contracts

## Design Rules

- lower layers must not depend on higher layers
- shared utilities must avoid application-specific assumptions
- configuration should be loaded from files, then merged, then optionally overridden
- logging should be configurable without hard-coding global state
- every module should be safe to import without side effects

## Configuration Strategy

Configuration is profile-based. `configs/base.yaml` defines defaults, and environment-specific files override them. The loader merges nested mappings recursively so future distributed settings can be layered without redesigning the system.

## Logging Strategy

Logging is centralized through explicit configuration objects. The initial implementation supports console and file handlers and leaves room for future experiment and training log sinks.
