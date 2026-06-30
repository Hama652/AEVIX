"""Validate the AEVIX foundation repository."""

from __future__ import annotations

import sys
from pathlib import Path
from tempfile import TemporaryDirectory


def _ensure_src_on_path() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src_path = repo_root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


def main() -> int:
    _ensure_src_on_path()

    from aevix.config import load_configuration
    from aevix.logging import LoggingConfiguration, configure_logging
    from aevix.registry import Registry
    from aevix.utils import CheckpointManager, CheckpointManifest, seed_everything

    bundle = load_configuration("testing")
    seed_everything(int(bundle.data["runtime"]["seed"]))

    logging_settings = LoggingConfiguration.from_mapping(bundle.data["logging"])
    logger = configure_logging(logging_settings)

    registry: Registry[str] = Registry()
    registry.register("validation", "ok")

    with TemporaryDirectory() as temporary_directory:
        checkpoint_manager = CheckpointManager(Path(temporary_directory))
        manifest = CheckpointManifest(
            name="validation",
            step=1,
            metadata={"profile": bundle.profile},
        )
        manifest_path = checkpoint_manager.save_manifest(manifest)
        restored_manifest = checkpoint_manager.load_manifest(manifest_path)

    if restored_manifest.name != "validation":
        raise RuntimeError("Checkpoint validation failed.")
    if not registry.contains("validation"):
        raise RuntimeError("Registry validation failed.")

    logger.info("AEVIX foundation validation completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
