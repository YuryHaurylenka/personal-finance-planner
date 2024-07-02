from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.database import Base, db_helper
from src.database.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(title="personal-finance-planner", lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
