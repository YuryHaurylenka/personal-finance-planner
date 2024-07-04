from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from src.views.user import router as user_router
from src.views.transaction import router as transaction_router
from src.views.goal import router as goal_router
from src.views.category import router as category_router
from src.views.budget import router as budget_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="personal-finance-planner", lifespan=lifespan)
app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(goal_router)
app.include_router(category_router)
app.include_router(budget_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
