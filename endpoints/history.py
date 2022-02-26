from fastapi import APIRouter

from db_config import db
from models.history_models import HistoryPost

router = APIRouter()

#Функция присылающая историю выражений из БД по лимиту
@router.post("/history")
async def history_post(body: HistoryPost):
    db_result = await db.expression_success(body.limit)

    return db_result