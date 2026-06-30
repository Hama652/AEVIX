"""Health endpoint for the dashboard backend."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from ...core.settings import DashboardSettings
from ..contracts import DashboardRoute, DashboardServiceName
from ..dependencies import get_settings

router = APIRouter(tags=["health"])


@router.get(DashboardRoute.HEALTH, name="health")
async def health(
    settings: Annotated[DashboardSettings, Depends(get_settings)],
) -> dict[str, str]:
    """Return the health status of the dashboard backend."""

    return {
        "service": DashboardServiceName.API,
        "status": "healthy",
        "environment": settings.environment,
    }
