from fastapi import APIRouter

from db_config import db
from models.history_models import HistoryPost, HistoryRespones

router = APIRouter()

@router.post("/history")
async def history_post(body: HistoryPost):
    db_result = await db.expression_success(body.limit)

    return db_result