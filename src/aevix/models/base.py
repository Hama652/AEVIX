"""Model-facing base contracts without implementing any model logic."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass(slots=True, frozen=True)
class ModelMetadata:
    """Metadata that describes a model family or artifact."""

    name: str
    family: str
    version: str = "0.1.0"
    parameter_count: int = 0
    tags: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class ModelProtocol(Protocol):
    """Minimal model contract for future PyTorch integration."""

    def state_dict(self) -> Mapping[str, Any]:
        """Return a serializable model state."""

    def load_state_dict(self, state: Mapping[str, Any]) -> None:
        """Load a previously serialized model state."""


@runtime_checkable
class ModelFactory(Protocol):
    """Callable that produces a model instance from configuration."""

    def __call__(self, config: Mapping[str, Any]) -> ModelProtocol:
        """Create a model instance."""
