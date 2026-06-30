"""Core component primitives for AEVIX."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True, frozen=True)
class ComponentMetadata:
    """Metadata that describes an AEVIX component."""

    name: str
    version: str = "0.1.0"
    description: str = ""
    owner: str = "AEVIX"
    tags: tuple[str, ...] = ()
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


class AevixComponent(ABC):
    """Base class for structured repository components."""

    def __init__(self, metadata: ComponentMetadata) -> None:
        self._metadata = metadata

    @property
    def metadata(self) -> ComponentMetadata:
        """Return the component metadata."""

        return self._metadata

    @property
    def name(self) -> str:
        """Return the component name."""

        return self._metadata.name

    @abstractmethod
    def validate(self) -> None:
        """Validate the component before use."""

    def to_dict(self) -> dict[str, Any]:
        """Serialize the component metadata to a dictionary."""

        return asdict(self._metadata)
