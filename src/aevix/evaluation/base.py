"""Evaluation-facing base contracts without implementing benchmarks."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass(slots=True, frozen=True)
class EvaluationCase:
    """An evaluation input and its expected output."""

    name: str
    inputs: Mapping[str, Any]
    expected_output: Any | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True, frozen=True)
class EvaluationResult:
    """Structured evaluation output."""

    name: str
    passed: bool
    score: float = 0.0
    details: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class Evaluator(Protocol):
    """Minimal evaluator contract for future benchmarks."""

    def evaluate(self, case: EvaluationCase) -> EvaluationResult:
        """Evaluate a single case and return a structured result."""
