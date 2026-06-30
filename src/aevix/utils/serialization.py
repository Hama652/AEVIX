"""Serialization helpers for JSON-compatible data."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, cast

from aevix.utils.filesystem import ensure_parent_directory


def to_json_text(value: Any, *, indent: int = 2) -> str:
    """Serialize a value to formatted JSON text."""

    return json.dumps(_normalize_value(value), indent=indent, sort_keys=True)


def from_json_text(text: str) -> Any:
    """Deserialize JSON text."""

    return json.loads(text)


def write_json(path: Path, value: Any, *, indent: int = 2) -> None:
    """Write JSON data to a file."""

    ensure_parent_directory(path)
    path.write_text(to_json_text(value, indent=indent), encoding="utf-8")


def read_json(path: Path) -> Any:
    """Read JSON data from a file."""

    return from_json_text(path.read_text(encoding="utf-8"))


def _normalize_value(value: Any) -> Any:
    if is_dataclass(value):
        return _normalize_value(asdict(cast(Any, value)))
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(key): _normalize_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_normalize_value(item) for item in value]
    if isinstance(value, tuple):
        return [_normalize_value(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value
