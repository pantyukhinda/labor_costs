from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from core.config import settings
from admin_user import run_bootstrap

from tasks.router import router as router_tasks
from organizations.router import router as router_organizations
from activity_types.router import router as router_activity_types
from divisions.router import router as router_divisions
from users.router import router as router_users
from projects.router import router as router_projects

from pages.router import router as pages_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await run_bootstrap()
    yield


app = FastAPI(title=settings.run.title, lifespan=lifespan)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/pages/", status_code=302)


static_dir = Path(__file__).resolve().parent / "static"
if static_dir.is_dir():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

app.include_router(router_users)
app.include_router(router_tasks)
app.include_router(router_organizations)
app.include_router(router_activity_types)
app.include_router(router_divisions)
app.include_router(router_projects)

app.include_router(pages_router)


if __name__ == "__main__":
    uvicorn.run(
        f"{__name__}:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
# TODO: Change main exceptions with custom exceptions
