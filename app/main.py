import uvicorn
from fastapi import FastAPI


from tasks.router import router as router_tasks
from organizations.router import router as router_organizations
from activity_types.router import router as router_activity_types
from divisions.router import router as router_divisions
from users.router import router as router_users
from projects.router import router as router_projects


app = FastAPI()
app.include_router(router_users)
app.include_router(router_tasks)
app.include_router(router_organizations)
app.include_router(router_activity_types)
app.include_router(router_divisions)
app.include_router(router_projects)


if __name__ == "__main__":
    uvicorn.run(
        f"{__name__}:app",
        host="127.0.0.1",
        port=8001,
        reload=True,
    )
