"""Timing helpers for infrastructure code."""

from __future__ import annotations

from collections.abc import Callable
from contextlib import AbstractContextManager
from dataclasses import dataclass, field
from time import perf_counter
from types import TracebackType
from typing import Literal, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class Timer(AbstractContextManager["Timer"]):
    """Measure elapsed wall-clock time."""

    label: str = "operation"
    start_time: float = field(init=False, default=0.0)
    end_time: float | None = field(init=False, default=None)

    def __enter__(self) -> Timer:
        self.start_time = perf_counter()
        self.end_time = None
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> Literal[False]:
        self.end_time = perf_counter()
        return False

    @property
    def elapsed_seconds(self) -> float:
        """Return the measured elapsed time."""

        end_time = self.end_time if self.end_time is not None else perf_counter()
        return end_time - self.start_time


def measure[T](
    callable_object: Callable[..., T], *args: object, **kwargs: object
) -> tuple[T, float]:
    """Measure a callable and return its result with elapsed seconds."""

    with Timer() as timer:
        result = callable_object(*args, **kwargs)
    return result, timer.elapsed_seconds
