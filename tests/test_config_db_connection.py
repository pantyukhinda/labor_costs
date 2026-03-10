from __future__ import annotations

import importlib
import os

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine


def _get_test_db_settings() -> dict[str, str]:
    return {
        "host": os.getenv("TEST_DB_HOST", "127.0.0.1"),
        "port": os.getenv("TEST_DB_PORT", "5432"),
        "name": os.getenv("TEST_DB_NAME", "labor_costs_test"),
        "user": os.getenv("TEST_DB_USER", "postgres"),
        "password": os.getenv("TEST_DB_PASSWORD", "postgres"),
    }


def _set_required_settings_env(*, monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Settings в проекте создаётся при импорте модуля (`settings = Settings()`).
    Поэтому env задаём перед `importlib.reload(...)`.
    """
    db = _get_test_db_settings()

    monkeypatch.setenv("APP_CONFIG__DB__HOST", db["host"])
    monkeypatch.setenv("APP_CONFIG__DB__PORT", str(db["port"]))
    monkeypatch.setenv("APP_CONFIG__DB__NAME", db["name"])
    monkeypatch.setenv("APP_CONFIG__DB__USER", db["user"])
    monkeypatch.setenv("APP_CONFIG__DB__PASSWORD", db["password"])
    monkeypatch.setenv("APP_CONFIG__DB__ECHO", "false")
    monkeypatch.setenv("APP_CONFIG__DB__ECHO_POOL", "false")
    monkeypatch.setenv("APP_CONFIG__DB__POOL_SIZE", "1")
    monkeypatch.setenv("APP_CONFIG__DB__MAX_OVERFLOW", "0")

    monkeypatch.setenv("APP_CONFIG__RUN__TITLE", "test")
    monkeypatch.setenv("APP_CONFIG__RUN__HOST", "127.0.0.1")
    monkeypatch.setenv("APP_CONFIG__RUN__PORT", "8000")
    monkeypatch.setenv("APP_CONFIG__RUN__RELOAD", "false")

    monkeypatch.setenv("APP_CONFIG__AUTH__KEY", "test-key")
    monkeypatch.setenv("APP_CONFIG__AUTH__ALGORITHM", "HS256")

    monkeypatch.setenv("APP_CONFIG__PGADMIN__EMAIL", "pgadmin@example.com")
    monkeypatch.setenv("APP_CONFIG__PGADMIN__PASSWORD", "pgadmin-password")
    monkeypatch.setenv("APP_CONFIG__PGADMIN__PORT", "5050")

    monkeypatch.setenv("APP_CONFIG__ADMIN__EMAIL", "admin@example.com")
    monkeypatch.setenv("APP_CONFIG__ADMIN__PASSWORD", "admin-password")


@pytest.mark.asyncio
async def test_settings_db_async_url_connects(monkeypatch: pytest.MonkeyPatch) -> None:
    if os.getenv("RUN_DB_INTEGRATION_TESTS") not in {"1", "true", "yes"}:
        pytest.skip("Set RUN_DB_INTEGRATION_TESTS=1 to run integration DB tests")

    _set_required_settings_env(monkeypatch=monkeypatch)

    import app.core.config.config as config_module

    importlib.reload(config_module)
    settings = config_module.settings

    engine = create_async_engine(
        str(settings.db.async_url),
        pool_pre_ping=True,
        pool_size=1,
        max_overflow=0,
    )

    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            assert result.scalar_one() == 1
    finally:
        await engine.dispose()

