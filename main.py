import uvicorn
from fastapi import FastAPI

from app.routers.task import router as router_tasks
from app.routers.organization import router as router_organizations

app = FastAPI()
app.include_router(router_tasks)
app.include_router(router_organizations)


if __name__ == "__main__":
    uvicorn.run(
        f"{__name__}:app",
        host="127.0.0.1",
        port=8001,
        reload=True,
    )
