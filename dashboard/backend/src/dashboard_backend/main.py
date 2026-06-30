"""Executable entry point for the dashboard backend."""

from __future__ import annotations

import uvicorn

from .app import create_app

app = create_app()


def main() -> None:
    """Run the dashboard backend with Uvicorn."""

    settings = app.state.settings
    uvicorn.run(
        "dashboard_backend.main:app",
        host=settings.host,
        port=settings.port,
        reload=False,
        log_level=settings.log_level.lower(),
    )


if __name__ == "__main__":
    main()
