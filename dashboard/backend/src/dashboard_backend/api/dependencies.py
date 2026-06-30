"""FastAPI dependencies for the dashboard backend."""

from __future__ import annotations

from fastapi import Request, WebSocket

from dashboard_backend.core.security import DashboardAuthenticationService, DashboardPrincipal
from dashboard_backend.core.settings import DashboardSettings
from dashboard_backend.core.websocket import DashboardWebSocketHub


def get_settings(request: Request) -> DashboardSettings:
    """Return the application settings stored on the FastAPI app."""

    return request.app.state.settings


def get_authentication_service(request: Request) -> DashboardAuthenticationService:
    """Return the placeholder authentication service."""

    return request.app.state.authentication_service


def get_websocket_hub_from_request(request: Request) -> DashboardWebSocketHub:
    """Return the shared websocket hub."""

    return request.app.state.websocket_hub


def get_websocket_hub_from_websocket(websocket: WebSocket) -> DashboardWebSocketHub:
    """Return the shared websocket hub for websocket routes."""

    return websocket.app.state.websocket_hub


def get_current_principal(request: Request) -> DashboardPrincipal:
    """Return the current placeholder user principal."""

    service = get_authentication_service(request)
    return service.current_principal()
