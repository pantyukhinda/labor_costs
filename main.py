import uvicorn
from fastapi import FastAPI
from app.tasks.router import router as router_tasks
from app.organisations.router import router as router_organisations

app = FastAPI()
app.include_router(router_tasks)
app.include_router(router_organisations)


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", host="127.0.0.1", port=8001, reload=True)
