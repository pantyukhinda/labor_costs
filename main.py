import uvicorn
from fastapi import FastAPI

from app.routers.task import router as router_tasks
from app.routers.organization import router as router_organizations
from app.routers.activity_type import router as router_activity_types
from app.routers.division import router as router_divisions
from app.routers.user import router as router_users
from app.routers.project import router as router_projects

app = FastAPI()
app.include_router(router_tasks)
app.include_router(router_organizations)
app.include_router(router_activity_types)
app.include_router(router_divisions)
app.include_router(router_users)
app.include_router(router_projects)


if __name__ == "__main__":
    uvicorn.run(
        f"{__name__}:app",
        host="127.0.0.1",
        port=8001,
        reload=True,
    )
