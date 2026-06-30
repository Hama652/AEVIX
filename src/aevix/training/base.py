"""Training-facing base contracts without implementing a training loop."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any, Protocol, runtime_checkable


class TrainingStage(StrEnum):
    """High-level training lifecycle stages."""

    INITIALIZATION = "initialization"
    PREPARATION = "preparation"
    TRAINING = "training"
    VALIDATION = "validation"
    CHECKPOINTING = "checkpointing"
    COMPLETED = "completed"


@dataclass(slots=True, frozen=True)
class TrainingRunMetadata:
    """Metadata describing a training run."""

    name: str
    stage: TrainingStage = TrainingStage.INITIALIZATION
    seed: int = 42
    output_dir: Path | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True, frozen=True)
class TrainingState:
    """Mutable training progress captured as a snapshot."""

    epoch: int = 0
    step: int = 0
    loss: float | None = None
    metrics: dict[str, float] = field(default_factory=dict)


@runtime_checkable
class TrainingController(Protocol):
    """Minimal contract for future orchestration logic."""

    def initialize(self) -> None:
        """Prepare the runtime for training."""

    def snapshot(self) -> Mapping[str, Any]:
        """Return a serializable state snapshot."""
