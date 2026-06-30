"""Path resolution helpers for AEVIX."""

from __future__ import annotations

from pathlib import Path


def repository_root() -> Path:
    """Return the repository root directory."""

    return Path(__file__).resolve().parents[3]


def src_root() -> Path:
    """Return the source root directory."""

    return repository_root() / "src"


def resolve_repo_path(*parts: str) -> Path:
    """Resolve a path relative to the repository root."""

    return repository_root().joinpath(*parts)


def configs_root() -> Path:
    """Return the configuration directory."""

    return repository_root() / "configs"
