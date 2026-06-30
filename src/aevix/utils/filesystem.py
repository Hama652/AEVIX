"""Filesystem helpers used by the repository foundation."""

from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path) -> Path:
    """Create a directory if it does not exist and return it."""

    path.mkdir(parents=True, exist_ok=True)
    return path


def ensure_parent_directory(path: Path) -> Path:
    """Ensure the parent directory for a file exists."""

    ensure_directory(path.parent)
    return path


def atomic_write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    """Write text to disk atomically using a temporary sibling file."""

    ensure_parent_directory(path)
    temporary_path = path.with_name(f".{path.name}.tmp")
    temporary_path.write_text(content, encoding=encoding)
    temporary_path.replace(path)


def read_text(path: Path, encoding: str = "utf-8") -> str:
    """Read text from a file path."""

    return path.read_text(encoding=encoding)


def path_exists(path: Path) -> bool:
    """Return whether a path exists on disk."""

    return path.exists()
