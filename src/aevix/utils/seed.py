"""Reproducibility helpers."""

from __future__ import annotations

import os
import random
from dataclasses import dataclass
from typing import Any

torch_module: Any | None
try:
    import torch as _torch
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    torch_module = None
else:
    torch_module = _torch


@dataclass(slots=True, frozen=True)
class SeedState:
    """Captured seeding information for a process."""

    seed: int
    deterministic: bool


def seed_everything(seed: int, deterministic: bool = True) -> SeedState:
    """Seed the Python runtime and optional numerical libraries."""

    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

    if torch_module is not None:
        torch_module.manual_seed(seed)
        if torch_module.cuda.is_available():
            torch_module.cuda.manual_seed_all(seed)
        torch_module.backends.cudnn.deterministic = deterministic
        torch_module.backends.cudnn.benchmark = not deterministic

    return SeedState(seed=seed, deterministic=deterministic)
