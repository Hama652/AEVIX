# AEVIX Architectural Decisions

## ADR-001: Use a typed `src` layout

Decision: keep importable code under `src/aevix`.

Reasoning: this prevents accidental implicit imports from the repository root and matches the long-term packaging strategy.

## ADR-002: Make configuration file-driven

Decision: use YAML files for profile-based configuration.

Reasoning: it keeps environment-specific settings explicit, reviewable, and easy to layer as the platform grows.

## ADR-003: Separate infrastructure from model logic

Decision: keep foundation concerns such as logging, paths, registries, and checkpoint metadata independent from any future model implementation.

Reasoning: the model stack will evolve faster than the platform layer, so the repository needs stable boundaries.
