from fastapi import APIRouter

from models.calc_models import CalcPost

router = APIRouter()

@router.post("/calc")
async def calc_post(body: CalcPost):
    respones = 0
    parametr = body.dict
    return{"Успех":"Успешный"}
