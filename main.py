from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.responses import RedirectResponse

from src.core.db_helper import db_helper
from src.views import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
app.include_router(router_v1)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
