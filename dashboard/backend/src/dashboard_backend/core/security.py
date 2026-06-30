"""Authentication placeholder services for the dashboard backend."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True, frozen=True)
class DashboardPrincipal:
    """Placeholder authenticated identity used for future auth integration."""

    subject: str = "anonymous"
    display_name: str = "Guest"
    authenticated: bool = False


class AuthenticationBackend(Protocol):
    """Contract for future authentication providers."""

    def authenticate(self, token: str) -> DashboardPrincipal:
        """Authenticate a bearer token and return a principal."""


class DashboardAuthenticationService:
    """Placeholder authentication service for the dashboard backend."""

    def __init__(self, enabled: bool, provider_name: str) -> None:
        self._enabled = enabled
        self._provider_name = provider_name

    @property
    def enabled(self) -> bool:
        """Return whether authentication is enabled."""

        return self._enabled

    @property
    def provider_name(self) -> str:
        """Return the configured provider name."""

        return self._provider_name

    def current_principal(self) -> DashboardPrincipal:
        """Return the current placeholder principal."""

        return DashboardPrincipal()
