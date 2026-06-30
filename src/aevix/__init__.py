"""AEVIX foundation package."""

from __future__ import annotations

__version__ = "0.1.0"

from aevix.config import ConfigurationBundle, load_configuration
from aevix.logging import LoggingConfiguration, configure_logging

__all__ = [
    "ConfigurationBundle",
    "LoggingConfiguration",
    "__version__",
    "configure_logging",
    "load_configuration",
]
