"""Shared constants for the dashboard API surface."""

from __future__ import annotations

from enum import StrEnum

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"


class DashboardServiceName(StrEnum):
    """Named dashboard services."""

    API = "dashboard-api"
    WEB = "dashboard-web"


class DashboardRoute(StrEnum):
    """Canonical API routes for the dashboard foundation."""

    HEALTH = "/health"
    STATUS = "/status"
    AUTH_SESSION = "/auth/session"
    AUTH_ME = "/auth/me"
    WEBSOCKET = "/ws/dashboard"


class DashboardPageName(StrEnum):
    """Canonical dashboard page names."""

    DASHBOARD = "Dashboard"
    TRAINING = "Training"
    MODELS = "Models"
    DATASETS = "Datasets"
    EXPERIMENTS = "Experiments"
    CHECKPOINTS = "Checkpoints"
    CLOUD = "Cloud"
    SETTINGS = "Settings"
    LOGS = "Logs"
    ABOUT = "About"
