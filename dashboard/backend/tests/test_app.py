"""Dashboard backend application tests."""

from __future__ import annotations

from dashboard_backend.app import create_app
from dashboard_backend.core.settings import DashboardSettings
from fastapi.testclient import TestClient


def test_health_endpoint_returns_healthy_status() -> None:
    app = create_app(
        DashboardSettings(
            environment="testing",
            auth_enabled=False,
            cors_origins=["http://localhost:5173"],
        )
    )

    with TestClient(app) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_status_endpoint_returns_dashboard_shell_state() -> None:
    app = create_app(
        DashboardSettings(
            environment="testing",
            auth_enabled=False,
            cors_origins=["http://localhost:5173"],
        )
    )

    with TestClient(app) as client:
        response = client.get("/api/v1/status")

    assert response.status_code == 200
    payload = response.json()
    assert payload["training_status"] == "No active training"
    assert payload["experiments"] == "No active experiments"


def test_websocket_snapshot_is_sent() -> None:
    app = create_app(
        DashboardSettings(
            environment="testing",
            auth_enabled=False,
            cors_origins=["http://localhost:5173"],
        )
    )

    with TestClient(app) as client, client.websocket_connect("/api/v1/ws/dashboard") as websocket:
        message = websocket.receive_json()

    assert message["type"] == "snapshot"
    assert "dashboard" in message["payload"]["channels"]
