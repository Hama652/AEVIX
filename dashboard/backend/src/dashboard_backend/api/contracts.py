"""Dashboard backend API contracts and route constants."""

from __future__ import annotations

from enum import StrEnum

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"


class DashboardRoute(StrEnum):
    """Canonical dashboard backend routes."""

    HEALTH = "/health"
    STATUS = "/status"
    AUTH_SESSION = "/auth/session"
    AUTH_ME = "/auth/me"
    WEBSOCKET = "/ws/dashboard"


class DashboardServiceName(StrEnum):
    """Named dashboard backend services."""

    API = "dashboard-api"
    WEB = "dashboard-web"
