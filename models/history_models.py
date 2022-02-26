from unittest.mock import Base
from pydantic import BaseModel, validator


#Модель данных, которая принимает функция history_post
class HistoryPost(BaseModel):
    limit : int = 30

    @validator("limit")
    def limit_check(cls, v):
        if v < 0 or v > 30:
            raise ValueError("Вы ввели неправильный лимит")
        return v
