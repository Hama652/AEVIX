"""WebSocket infrastructure for the dashboard backend."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect


@dataclass(slots=True)
class WebSocketSnapshot:
    """Describe the current WebSocket connection state."""

    connections: int
    channels: list[str] = field(default_factory=list)


class DashboardWebSocketHub:
    """Manage dashboard WebSocket connections and placeholder broadcasts."""

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger
        self._connections: set[WebSocket] = set()

    @property
    def connection_count(self) -> int:
        """Return the number of active connections."""

        return len(self._connections)

    async def connect(self, websocket: WebSocket) -> None:
        """Accept and register a new WebSocket connection."""

        await websocket.accept()
        self._connections.add(websocket)
        self._logger.info("Dashboard websocket connected")

    def disconnect(self, websocket: WebSocket) -> None:
        """Remove a WebSocket connection from the hub."""

        self._connections.discard(websocket)
        self._logger.info("Dashboard websocket disconnected")

    async def send_snapshot(self, websocket: WebSocket) -> None:
        """Send a minimal infrastructure snapshot to a client."""

        await websocket.send_json(
            {
                "type": "snapshot",
                "payload": {
                    "connections": self.connection_count,
                    "channels": ["dashboard", "logs", "status"],
                },
            }
        )

    async def run(self, websocket: WebSocket) -> None:
        """Handle a connected WebSocket until the client disconnects."""

        await self.connect(websocket)
        try:
            await self.send_snapshot(websocket)
            while True:
                await websocket.receive_text()
        except WebSocketDisconnect:
            self.disconnect(websocket)
