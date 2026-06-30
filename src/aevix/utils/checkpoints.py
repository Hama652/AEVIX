"""Checkpoint metadata and persistence helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from aevix.exceptions import CheckpointError
from aevix.utils.filesystem import ensure_directory
from aevix.utils.serialization import read_json, write_json


@dataclass(slots=True, frozen=True)
class CheckpointManifest:
    """Metadata describing a saved checkpoint."""

    name: str
    step: int
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    artifacts: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


class CheckpointManager:
    """Manage checkpoint metadata inside a dedicated directory."""

    def __init__(self, root: Path) -> None:
        self._root = ensure_directory(root)

    @property
    def root(self) -> Path:
        """Return the checkpoint root directory."""

        return self._root

    def checkpoint_directory(self, name: str, step: int) -> Path:
        """Resolve a canonical checkpoint directory path."""

        return self._root / name / f"step-{step:09d}"

    def save_manifest(self, manifest: CheckpointManifest) -> Path:
        """Save a checkpoint manifest to disk."""

        checkpoint_directory = self.checkpoint_directory(manifest.name, manifest.step)
        ensure_directory(checkpoint_directory)
        manifest_path = checkpoint_directory / "manifest.json"
        write_json(manifest_path, manifest)
        return manifest_path

    def load_manifest(self, manifest_path: Path) -> CheckpointManifest:
        """Load a checkpoint manifest from disk."""

        try:
            data = read_json(manifest_path)
        except OSError as exc:
            raise CheckpointError(f"Unable to load checkpoint manifest: {manifest_path}") from exc

        if not isinstance(data, dict):
            raise CheckpointError(f"Checkpoint manifest must contain a mapping: {manifest_path}")

        try:
            return CheckpointManifest(
                name=str(data["name"]),
                step=int(data["step"]),
                created_at=datetime.fromisoformat(str(data["created_at"])),
                artifacts=dict(data.get("artifacts", {})),
                metadata=dict(data.get("metadata", {})),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise CheckpointError(f"Invalid checkpoint manifest: {manifest_path}") from exc

    def latest_manifest(self, name: str) -> Path | None:
        """Return the most recent manifest for a checkpoint family."""

        family_root = self._root / name
        if not family_root.exists():
            return None

        manifests = sorted(family_root.glob("step-*/manifest.json"))
        return manifests[-1] if manifests else None
