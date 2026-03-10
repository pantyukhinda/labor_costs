# Тесты

## Интеграционный тест конфигурации БД

Тест `tests/test_config_db_connection.py` проверяет, что:

- `Settings()` корректно собирается из env (`APP_CONFIG__...`)
- `settings.db.async_url` рабочий
- SQLAlchemy async engine может подключиться к Postgres и выполнить `SELECT 1`

### Поднять тестовую Postgres

```bash
docker compose -f docker-compose.test.yml up -d
```

### Запустить тест

```bash
RUN_DB_INTEGRATION_TESTS=1 poetry run pytest -q
```

### Переопределить параметры подключения (опционально)

По умолчанию тест использует:

- host: `127.0.0.1`
- port: `5432`
- db: `labor_costs_test`
- user/password: `postgres/postgres`

Можно переопределить через env:

```bash
export TEST_DB_HOST=127.0.0.1
export TEST_DB_PORT=5432
export TEST_DB_NAME=labor_costs_test
export TEST_DB_USER=postgres
export TEST_DB_PASSWORD=postgres
```

