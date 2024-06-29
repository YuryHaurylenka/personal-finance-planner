from fastapi import APIRouter, FastAPI

app = FastAPI(title='personal-finance-planner')

user_router = APIRouter()


@app.get("/")
def top():
    return "personal-finance-planner"

