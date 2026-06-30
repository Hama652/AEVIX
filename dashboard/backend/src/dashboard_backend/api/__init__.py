"""Dashboard backend API package."""

from __future__ import annotations

from .contracts import API_PREFIX, API_VERSION, DashboardRoute, DashboardServiceName
from .router import api_router

__all__ = [
	"API_PREFIX",
	"API_VERSION",
	"DashboardRoute",
	"DashboardServiceName",
	"api_router",
]
