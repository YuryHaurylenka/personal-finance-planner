from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.views import (
    budget_router,
    category_router,
    fake_data_router,
    goal_router,
    transaction_router,
    user_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="personal-finance-planner", lifespan=lifespan)
app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(goal_router)
app.include_router(category_router)
app.include_router(budget_router)
app.include_router(fake_data_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
