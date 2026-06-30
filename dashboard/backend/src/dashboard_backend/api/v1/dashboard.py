"""Operational overview endpoints for the dashboard backend."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from ...core.security import DashboardPrincipal
from ...core.settings import DashboardSettings
from ...core.websocket import DashboardWebSocketHub
from ..contracts import DashboardRoute
from ..dependencies import get_current_principal, get_settings, get_websocket_hub_from_request

router = APIRouter(tags=["dashboard"])


@router.get(DashboardRoute.STATUS, name="status")
async def status(
    settings: Annotated[DashboardSettings, Depends(get_settings)],
    principal: Annotated[DashboardPrincipal, Depends(get_current_principal)],
    websocket_hub: Annotated[DashboardWebSocketHub, Depends(get_websocket_hub_from_request)],
) -> dict[str, object]:
    """Return the dashboard shell status without live model data."""

    return {
        "application": settings.application_name,
        "environment": settings.environment,
        "authentication_enabled": settings.auth_enabled,
        "current_user": {
            "subject": principal.subject,
            "display_name": principal.display_name,
            "authenticated": principal.authenticated,
        },
        "websocket_connections": websocket_hub.connection_count,
        "training_status": "No active training",
        "experiments": "No active experiments",
    }
