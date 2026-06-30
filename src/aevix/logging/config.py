"""Structured logging setup for AEVIX."""

from __future__ import annotations

import logging
from collections.abc import Mapping
from dataclasses import dataclass
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from aevix.exceptions import LoggingConfigurationError
from aevix.utils.filesystem import ensure_directory


@dataclass(slots=True, frozen=True)
class LoggingConfiguration:
    """Configuration for the repository logging stack."""

    logger_name: str = "aevix"
    level: str = "INFO"
    console: bool = True
    file: bool = True
    file_path: Path | None = None
    format: str = "%(asctime)s %(levelname)s %(name)s %(message)s"
    date_format: str = "%Y-%m-%d %H:%M:%S"
    max_bytes: int = 10_485_760
    backup_count: int = 5

    @classmethod
    def from_mapping(cls, mapping: Mapping[str, Any]) -> LoggingConfiguration:
        """Create a logging configuration from a dictionary."""

        rotation = mapping.get("rotation", {})
        file_path_value = mapping.get("file_path")
        file_path = Path(file_path_value) if file_path_value else None
        return cls(
            logger_name=str(mapping.get("logger_name", "aevix")),
            level=str(mapping.get("level", "INFO")),
            console=bool(mapping.get("console", True)),
            file=bool(mapping.get("file", True)),
            file_path=file_path,
            format=str(mapping.get("format", "%(asctime)s %(levelname)s %(name)s %(message)s")),
            date_format=str(mapping.get("date_format", "%Y-%m-%d %H:%M:%S")),
            max_bytes=int(rotation.get("max_bytes", 10_485_760)),
            backup_count=int(rotation.get("backup_count", 5)),
        )


def configure_logging(settings: LoggingConfiguration) -> logging.Logger:
    """Configure and return the named AEVIX logger."""

    logger = logging.getLogger(settings.logger_name)
    logger.setLevel(_resolve_level(settings.level))
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(settings.format, datefmt=settings.date_format)

    if settings.console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if settings.file:
        if settings.file_path is None:
            raise LoggingConfigurationError(
                "A file path is required when file logging is enabled."
            )
        ensure_directory(settings.file_path.parent)
        file_handler = RotatingFileHandler(
            settings.file_path,
            maxBytes=settings.max_bytes,
            backupCount=settings.backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if not logger.handlers:
        logger.addHandler(logging.NullHandler())

    return logger


def _resolve_level(level_name: str) -> int:
    resolved_level = logging.getLevelName(level_name.upper())
    if isinstance(resolved_level, int):
        return resolved_level
    raise LoggingConfigurationError(f"Unknown logging level: {level_name}")
