"""Tests for YAML configuration loading."""

from __future__ import annotations

from pathlib import Path

from aevix.config import load_configuration


def test_load_configuration_merges_profile_settings(tmp_path: Path) -> None:
    config_dir = tmp_path / "configs"
    config_dir.mkdir()
    (config_dir / "base.yaml").write_text(
        """
project:
  name: AEVIX
logging:
  level: INFO
  rotation:
    max_bytes: 1
    backup_count: 1
paths:
  logs: logs
""".strip(),
        encoding="utf-8",
    )
    (config_dir / "testing.yaml").write_text(
        """
logging:
  level: WARNING
  rotation:
    backup_count: 9
paths:
  logs: logs/testing
""".strip(),
        encoding="utf-8",
    )

    bundle = load_configuration("testing", config_dir=config_dir)

    assert bundle.profile == "testing"
    assert bundle.data["logging"]["level"] == "WARNING"
    assert bundle.data["logging"]["rotation"]["max_bytes"] == 1
    assert bundle.data["logging"]["rotation"]["backup_count"] == 9
    assert bundle.data["paths"]["logs"] == "logs/testing"
