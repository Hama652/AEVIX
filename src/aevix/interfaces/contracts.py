"""Protocols that define cross-layer contracts."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Validatable(Protocol):
    """Object that can validate its own state."""

    def validate(self) -> None:
        """Validate the object's state."""


@runtime_checkable
class Serializable(Protocol):
    """Object that can be represented as a mapping."""

    def to_dict(self) -> Mapping[str, Any]:
        """Return a serializable representation."""


@runtime_checkable
class Configurable(Protocol):
    """Object that can be configured from a mapping."""

    def configure(self, config: Mapping[str, Any]) -> None:
        """Apply the provided configuration."""


@runtime_checkable
class Persistable(Protocol):
    """Object that can be written to and restored from disk."""

    def save(self, path: Path) -> None:
        """Persist the object to the provided path."""

    @classmethod
    def load(cls, path: Path) -> Any:
        """Restore an object from the provided path."""
