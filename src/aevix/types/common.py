"""Shared type aliases used across the repository."""

from __future__ import annotations

from typing import Any

type JSONScalar = str | int | float | bool | None
type JSONValue = JSONScalar | list[JSONValue] | dict[str, JSONValue]
type JSONObject = dict[str, JSONValue]
type MappingStrAny = dict[str, Any]
type PathLikeStr = str
