"""FastAPI application factory for the dashboard backend."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import API_PREFIX, DashboardServiceName, api_router
from .core.logging import DashboardLoggingProfile, configure_logging
from .core.security import DashboardAuthenticationService
from .core.settings import DashboardSettings, load_settings
from .core.websocket import DashboardWebSocketHub


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifespan hook for startup and shutdown initialization."""

    yield


def create_app(settings: DashboardSettings | None = None) -> FastAPI:
    """Create the FastAPI application used by the dashboard backend."""

    resolved_settings = settings or load_settings()
    logger = configure_logging(
        DashboardLoggingProfile(
            logger_name=DashboardServiceName.API,
            level=resolved_settings.log_level,
            log_directory=resolved_settings.data_directory / "logs",
        )
    )
    application = FastAPI(
        title=resolved_settings.application_name,
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=resolved_settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.state.settings = resolved_settings
    application.state.logger = logger
    application.state.authentication_service = DashboardAuthenticationService(
        enabled=resolved_settings.auth_enabled,
        provider_name=resolved_settings.auth_provider_name,
    )
    application.state.websocket_hub = DashboardWebSocketHub(logger)
    application.include_router(api_router, prefix=API_PREFIX)
    return application
