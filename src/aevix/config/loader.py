"""YAML configuration loading for AEVIX."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from aevix.exceptions import ConfigurationError

yaml_module: Any | None
_YAML_IMPORT_ERROR: Exception | None
try:
    import yaml as _yaml
except ModuleNotFoundError as exc:  # pragma: no cover - defensive import guard
    yaml_module = None
    _YAML_IMPORT_ERROR = exc
else:
    yaml_module = _yaml
    _YAML_IMPORT_ERROR = None


@dataclass(slots=True, frozen=True)
class ConfigurationBundle:
    """Resolved configuration data and the files it came from."""

    profile: str
    data: dict[str, Any]
    source_paths: tuple[Path, ...]


DEFAULT_CONFIG_DIR = Path(__file__).resolve().parents[3] / "configs"


def load_configuration(
    profile: str = "development",
    config_dir: Path | None = None,
    overrides: Mapping[str, Any] | None = None,
) -> ConfigurationBundle:
    """Load and merge the base configuration with a profile override.

    Args:
        profile: Configuration profile name.
        config_dir: Optional directory containing YAML configuration files.
        overrides: Optional final override mapping.

    Returns:
        A configuration bundle containing the merged data and source paths.

    Raises:
        ConfigurationError: If a configuration file is missing or invalid.
    """

    _ensure_yaml_available()

    resolved_config_dir = config_dir or DEFAULT_CONFIG_DIR
    normalized_profile = profile.strip().lower()
    base_path = resolved_config_dir / "base.yaml"
    profile_path = resolved_config_dir / f"{normalized_profile}.yaml"

    base_config = _load_yaml_mapping(base_path)
    profile_config = _load_yaml_mapping(profile_path)
    merged_config = _deep_merge(base_config, profile_config)
    if overrides is not None:
        merged_config = _deep_merge(merged_config, overrides)

    return ConfigurationBundle(
        profile=normalized_profile,
        data=dict(merged_config),
        source_paths=(base_path, profile_path),
    )


def _ensure_yaml_available() -> None:
    if yaml_module is None:
        raise ConfigurationError(
            "PyYAML is required to load configuration files. "
            "Install the project development dependencies before running AEVIX."
        ) from _YAML_IMPORT_ERROR


def _load_yaml_mapping(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigurationError(f"Configuration file not found: {path}")
    try:
        assert yaml_module is not None
        with path.open("r", encoding="utf-8") as file_handle:
            loaded = yaml_module.safe_load(file_handle) or {}
    except OSError as exc:
        raise ConfigurationError(f"Unable to read configuration file: {path}") from exc
    except Exception as exc:  # pragma: no cover - PyYAML formats its own errors
        raise ConfigurationError(f"Invalid YAML in configuration file: {path}") from exc

    if not isinstance(loaded, Mapping):
        raise ConfigurationError(f"Configuration file must contain a mapping: {path}")
    return dict(loaded)


def _deep_merge(left: Mapping[str, Any], right: Mapping[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(left)
    for key, right_value in right.items():
        left_value = merged.get(key)
        if isinstance(left_value, Mapping) and isinstance(right_value, Mapping):
            merged[key] = _deep_merge(left_value, right_value)
        else:
            merged[key] = right_value
    return merged
