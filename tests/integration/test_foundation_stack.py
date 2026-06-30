"""Integration tests for the AEVIX foundation stack."""

from __future__ import annotations

from pathlib import Path

from aevix.config import load_configuration
from aevix.logging import LoggingConfiguration, configure_logging
from aevix.utils import CheckpointManager, CheckpointManifest, seed_everything


def test_configuration_logging_and_checkpoint_round_trip(tmp_path: Path) -> None:
    bundle = load_configuration("testing")
    logging_settings = LoggingConfiguration.from_mapping(bundle.data["logging"])
    logger = configure_logging(logging_settings)
    logger.info("integration-check")

    seed_state = seed_everything(int(bundle.data["runtime"]["seed"]))
    assert seed_state.seed == 1234

    checkpoint_manager = CheckpointManager(tmp_path / "checkpoints")
    manifest = CheckpointManifest(
        name="integration",
        step=7,
        metadata={"profile": bundle.profile},
    )
    manifest_path = checkpoint_manager.save_manifest(manifest)
    restored_manifest = checkpoint_manager.load_manifest(manifest_path)

    assert restored_manifest.name == manifest.name
    assert restored_manifest.step == manifest.step
    assert restored_manifest.metadata["profile"] == "testing"
