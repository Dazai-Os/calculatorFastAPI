from fastapi import APIRouter

from models.history_models import HistoryPost

router = APIRouter()

@router.post("/history")
async def history_post(body: HistoryPost):
    return{"Успех": "Успешный"}