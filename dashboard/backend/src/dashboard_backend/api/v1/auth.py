"""Authentication placeholder endpoints."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, status

from ...core.security import DashboardAuthenticationService, DashboardPrincipal
from ..contracts import DashboardRoute
from ..dependencies import get_authentication_service, get_current_principal

router = APIRouter(tags=["authentication"])


@router.post(
    DashboardRoute.AUTH_SESSION,
    name="create-auth-session",
    status_code=status.HTTP_501_NOT_IMPLEMENTED,
)
async def create_auth_session(
    authentication_service: Annotated[
        DashboardAuthenticationService,
        Depends(get_authentication_service),
    ],
) -> dict[str, str]:
    """Placeholder authentication endpoint for future session issuance."""

    return {
        "message": "Authentication is not implemented yet.",
        "provider": authentication_service.provider_name,
    }


@router.get(DashboardRoute.AUTH_ME, name="current-user")
async def current_user(
    principal: Annotated[DashboardPrincipal, Depends(get_current_principal)],
) -> dict[str, object]:
    """Return the current placeholder user profile."""

    return {
        "subject": principal.subject,
        "display_name": principal.display_name,
        "authenticated": principal.authenticated,
    }
