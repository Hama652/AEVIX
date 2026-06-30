"""Generic registry primitives."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import TypeVar

from aevix.exceptions import RegistryError

T = TypeVar("T")


@dataclass(slots=True)
class RegistryEntry[T]:
    """A named registry entry."""

    name: str
    value: T


class Registry[T]:
    """A small, explicit registry for controlled extensibility."""

    def __init__(self) -> None:
        self._entries: dict[str, T] = {}

    def register(self, name: str, value: T) -> T:
        """Register a value under a stable name."""

        normalized_name = self._normalize_name(name)
        if normalized_name in self._entries:
            raise RegistryError(f"Registry entry '{normalized_name}' is already registered.")
        self._entries[normalized_name] = value
        return value

    def unregister(self, name: str) -> T:
        """Remove a registered value and return it."""

        normalized_name = self._normalize_name(name)
        try:
            return self._entries.pop(normalized_name)
        except KeyError as exc:
            raise RegistryError(f"Registry entry '{normalized_name}' was not found.") from exc

    def get(self, name: str) -> T:
        """Return a registered value."""

        normalized_name = self._normalize_name(name)
        try:
            return self._entries[normalized_name]
        except KeyError as exc:
            raise RegistryError(f"Registry entry '{normalized_name}' was not found.") from exc

    def contains(self, name: str) -> bool:
        """Check whether a name is registered."""

        return self._normalize_name(name) in self._entries

    def items(self) -> Iterable[RegistryEntry[T]]:
        """Return registry entries as structured items."""

        return (RegistryEntry(name, value) for name, value in self._entries.items())

    def keys(self) -> Iterator[str]:
        """Return registered names."""

        return iter(self._entries)

    def values(self) -> Iterator[T]:
        """Return registered values."""

        return iter(self._entries.values())

    @staticmethod
    def _normalize_name(name: str) -> str:
        normalized_name = name.strip().lower()
        if not normalized_name:
            raise RegistryError("Registry names must not be empty.")
        return normalized_name
