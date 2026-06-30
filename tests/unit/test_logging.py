"""Tests for the structured logging foundation."""

from __future__ import annotations

from pathlib import Path

from aevix.logging import LoggingConfiguration, configure_logging


def test_configure_logging_writes_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "logs" / "aevix.log"
    settings = LoggingConfiguration(
        logger_name="aevix.tests.logging",
        level="INFO",
        console=False,
        file=True,
        file_path=log_file,
    )

    logger = configure_logging(settings)
    logger.info("hello from tests")

    for handler in logger.handlers:
        flush = getattr(handler, "flush", None)
        if callable(flush):
            flush()

    assert log_file.exists()
    assert "hello from tests" in log_file.read_text(encoding="utf-8")
