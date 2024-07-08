from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.views import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="personal-finance-planner", lifespan=lifespan)
app.include_router(router_v1)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
