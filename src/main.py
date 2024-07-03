import uvicorn
from fastapi import FastAPI

from src.api_v1 import router as router_v1
from src.database.config import settings

app = FastAPI(title="personal-finance-planner")
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def top():
    return "personal-finance-planner"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
