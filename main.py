import uvicorn
from fastapi import FastAPI, HTTPException

from db_config import db
from models.calc_models import CalcPost
from endpoints import calc
from endpoints import history


app = FastAPI()
app.include_router(calc.router)
app.include_router(history.router)


@app.on_event("startup")
async def startup():
    await db.create()
    await db.create_table_users()


if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, host = "127.0.0.1", reload = True)