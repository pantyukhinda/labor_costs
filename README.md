# Labor costs

## Product description

**Labor costs** is a web application for managing labor cost data. It provides:

- **Organizations** — company or unit records
- **Divisions** — hierarchical structure (e.g. directorate, department, sector, group)
- **Users** — employees linked to divisions
- **Projects** — projects per organization
- **Activity types** — types of work (e.g. development, testing, meetings)
- **Tasks** — time-tracked tasks linking users, projects, and activity types

The app exposes a FastAPI backend with REST-style endpoints and a web UI (Jinja2 templates) for organizations, projects, divisions, activity types, tasks, and user auth (login/register). Data is stored in PostgreSQL. A default admin user is created at startup.

---

## Launch instructions

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/) (or use `pip` with dependencies from `pyproject.toml`)
- Docker and Docker Compose (for running PostgreSQL and pgAdmin)

### 1. Clone and install dependencies

```bash
cd labor_costs
poetry install
# or: pip install -e .
```

### 2. Environment configuration

Copy the template and create a `.env` file in the project root:

```bash
cp env.template .env
```

Edit `.env` and set at least:

- **Database:** `APP_CONFIG__DB__HOST`, `APP_CONFIG__DB__NAME`, `APP_CONFIG__DB__PORT`, `APP_CONFIG__DB__USER`, `APP_CONFIG__DB__PASSWORD` (must match the Postgres service).
- **Application:** `APP_CONFIG__RUN__TITLE`, `APP_CONFIG__RUN__HOST`. Add if missing:
  - `APP_CONFIG__RUN__PORT=8000`
  - `APP_CONFIG__RUN__RELOAD=false` (or `true` for development).
- **Auth:** `APP_CONFIG__AUTH__KEY` (secret for JWT), `APP_CONFIG__AUTH__ALGORITHM=HS256`.
- **Admin user:** `APP_CONFIG__ADMIN__EMAIL`, `APP_CONFIG__ADMIN__PASSWORD` (superuser created at startup).
- **pgAdmin (optional):** `APP_CONFIG__PGADMIN__EMAIL`, `APP_CONFIG__PGADMIN__PASSWORD`, `APP_CONFIG__PGADMIN__PORT`.

### 3. Start PostgreSQL (and pgAdmin)

From the project root:

```bash
docker-compose up -d
```

PostgreSQL will listen on the port set in `APP_CONFIG__DB__PORT` (e.g. `5452`). pgAdmin will be on `APP_CONFIG__PGADMIN__PORT` (e.g. `5000`).

### 4. Run database migrations

```bash
cd app
alembic upgrade head
# or from project root: alembic -c alembic.ini upgrade head (ensure app or project root is on PYTHONPATH)
```

If you run Alembic from the project root, ensure the `app` directory is on `PYTHONPATH`, e.g.:

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/app"
alembic upgrade head
```

### 5. Start the application

From the **project root**, with `app` on the Python path:

```bash
poetry run python -m app.main
# or: cd app && poetry run python main.py
```

The API and UI will be available at:

- **Web UI:** `http://<APP_CONFIG__RUN__HOST>:<APP_CONFIG__RUN__PORT>/` (redirects to `/pages/`)
- **API docs:** `http://<APP_CONFIG__RUN__HOST>:<APP_CONFIG__RUN__PORT>/docs`

Default admin credentials are from `APP_CONFIG__ADMIN__EMAIL` and `APP_CONFIG__ADMIN__PASSWORD`.

---

## Filling the database with test data

Two options are available: an HTTP-based script and a DAO-based script.

### Option 1: Test data via HTTP API (`test_data.py`)

This script uses the application’s HTTP API (via ASGI), so **the app must be running** before you run it.

1. Start the app (see [Launch instructions](#launch-instructions)).
2. From the project root, run:

```bash
cd test/test_data
python test_data.py
```

It expects `constants.py` in the same directory to define at least:

- `ORGANIZATION_NAMES`
- `FIRST_NAMES`, `LAST_NAMES`, `PATRONYMICS`

It creates organizations, divisions, and users through the API (organizations and divisions first, then users). You may need to align `constants.py` with these names or add the missing lists.

### Option 2: Test data via DAO (`insesrt_data.py`)

This script inserts data directly via DAO layer (no HTTP). The database must be up and migrated; the app does **not** need to be running.

1. Ensure PostgreSQL is running and migrations are applied.
2. From the **project root**, ensure the `app` directory is on `PYTHONPATH`, then run the script from `test/test_data`:

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/app"
cd test/test_data
python insesrt_data.py
```

It uses `test/test_data/constants.py`, which provides generators for:

- **Organizations** (`N_ORG`), **divisions** (`N_DIV`), **users** (`N_USER`)
- **Projects** (`N_PROJ`), **activity types** (`N_ACT_TYPES`), **tasks** (`N_TASK`)

Data is created in order: organizations → divisions → users → projects → activity types → tasks. Constants at the top of `constants.py` control how many rows are generated. The script uses the same `.env` (and thus the same DB settings) as the app when the path is set so that `core.config` and `core.database` can be loaded.

**Note:** `insesrt_data.py` and `dao_base.py` assume that running from `test/test_data` with `app` on `PYTHONPATH` allows the app’s `core.database` and models to be imported. If you see import errors for `database` or `dao`, fix `dao_base.py` to use `from core.database import database` (and ensure `PYTHONPATH` includes the project root or `app` as appropriate).

---

## Project structure (overview)

- **`app/`** — FastAPI app: `main.py`, routers (users, tasks, organizations, activity_types, divisions, projects), pages, auth, models, DAOs, config, database.
- **`alembic/`** — Migrations for PostgreSQL.
- **`test/test_data/`** — Scripts and constants for seeding test data (`test_data.py`, `insesrt_data.py`, `constants.py`, `dao.py`, `dao_base.py`).
- **`env.template`** — Template for `.env` (copy to `.env` and fill in values).
- **`docker-compose.yaml`** — PostgreSQL and pgAdmin services.
