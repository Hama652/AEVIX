"""Structured logging for the dashboard backend."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from logging.config import dictConfig
from pathlib import Path


@dataclass(slots=True, frozen=True)
class DashboardLoggingProfile:
    """Logging configuration for the dashboard backend."""

    logger_name: str
    level: str
    log_directory: Path | None = None


def configure_logging(profile: DashboardLoggingProfile) -> logging.Logger:
    """Configure the dashboard backend logger hierarchy."""

    handlers: dict[str, dict[str, object]] = {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": profile.level,
        }
    }
    root_handlers = ["console"]

    if profile.log_directory is not None:
        profile.log_directory.mkdir(parents=True, exist_ok=True)
        handlers["file"] = {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": str(profile.log_directory / "dashboard-backend.log"),
            "formatter": "standard",
            "level": profile.level,
            "maxBytes": 10_485_760,
            "backupCount": 5,
            "encoding": "utf-8",
        }
        root_handlers.append("file")

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                }
            },
            "handlers": handlers,
            "loggers": {
                profile.logger_name: {
                    "handlers": root_handlers,
                    "level": profile.level,
                    "propagate": False,
                }
            },
        }
    )
    return logging.getLogger(profile.logger_name)
