"""Dashboard backend settings."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from dashboard.api import API_PREFIX


class DashboardSettings(BaseSettings):
    """Runtime settings for the dashboard backend."""

    application_name: str = "AEVIX Dashboard API"
    environment: Literal["development", "testing", "production"] = "development"
    api_prefix: str = API_PREFIX
    host: str = "127.0.0.1"
    port: int = 8000
    log_level: str = "INFO"
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])
    websocket_heartbeat_seconds: int = 30
    auth_enabled: bool = False
    auth_provider_name: str = "placeholder"
    frontend_url: str = "http://localhost:5173"
    data_directory: Path = Path("dashboard") / "data"

    model_config = SettingsConfigDict(
        env_prefix="AEVIX_DASHBOARD_",
        env_file=".env",
        extra="ignore",
        frozen=True,
    )


@lru_cache(maxsize=1)
def load_settings() -> DashboardSettings:
    """Load and cache dashboard settings from the environment."""

    return DashboardSettings()
