"""API router assembly for the dashboard backend."""

from __future__ import annotations

from fastapi import APIRouter

from .v1.auth import router as auth_router
from .v1.dashboard import router as dashboard_router
from .v1.health import router as health_router
from .v1.websocket import router as websocket_router

api_router = APIRouter()
api_router.include_router(health_router, prefix="")
api_router.include_router(dashboard_router, prefix="")
api_router.include_router(auth_router, prefix="")
api_router.include_router(websocket_router, prefix="")
