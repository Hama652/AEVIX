"""Environment variable helpers."""

from __future__ import annotations

import os
from pathlib import Path


def get_env(name: str, default: str | None = None) -> str | None:
    """Return a raw environment variable value."""

    return os.environ.get(name, default)


def get_bool_env(name: str, default: bool = False) -> bool:
    """Parse an environment variable as a boolean."""

    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_int_env(name: str, default: int | None = None) -> int | None:
    """Parse an environment variable as an integer."""

    value = os.environ.get(name)
    if value is None:
        return default
    return int(value.strip())


def get_path_env(name: str, default: Path | None = None) -> Path | None:
    """Parse an environment variable as a path."""

    value = os.environ.get(name)
    if value is None:
        return default
    return Path(value).expanduser()


def iter_prefixed_environment(prefix: str) -> dict[str, str]:
    """Return environment variables with the provided prefix removed."""

    normalized_prefix = prefix.upper()
    return {
        key[len(normalized_prefix) :].lower(): value
        for key, value in os.environ.items()
        if key.startswith(normalized_prefix)
    }
