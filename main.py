import uvicorn
from fastapi import FastAPI
from db_config import db


app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.create()
    await db.create_table_users()


@app.post("/calc")
async def calc_post():
    return {"message": "calc"}



if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, host = "127.0.0.1", reload = True)