"""WebSocket route for the dashboard backend."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, WebSocket

from ...core.websocket import DashboardWebSocketHub
from ..contracts import DashboardRoute
from ..dependencies import get_websocket_hub_from_websocket

router = APIRouter(tags=["websocket"])


@router.websocket(DashboardRoute.WEBSOCKET)
async def dashboard_socket(
    websocket: WebSocket,
    websocket_hub: Annotated[DashboardWebSocketHub, Depends(get_websocket_hub_from_websocket)],
) -> None:
    """Serve the dashboard websocket channel."""

    await websocket_hub.run(websocket)
