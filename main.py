import uvicorn
from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", host="127.0.0.1", port=8001, reload=True)
