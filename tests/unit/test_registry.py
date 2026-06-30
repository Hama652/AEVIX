"""Tests for the registry foundation."""

from __future__ import annotations

import pytest

from aevix.exceptions import RegistryError
from aevix.registry import Registry


def test_registry_registers_and_resolves_values() -> None:
    registry: Registry[str] = Registry()

    registry.register("Tokenizer", "value")

    assert registry.contains("tokenizer")
    assert registry.get("tokenizer") == "value"


def test_registry_rejects_duplicate_names() -> None:
    registry: Registry[str] = Registry()

    registry.register("model", "one")

    with pytest.raises(RegistryError):
        registry.register("MODEL", "two")
