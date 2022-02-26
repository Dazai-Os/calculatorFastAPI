from pydantic import BaseModel, validator

class HistoryPost(BaseModel):
    limit : int = 30

    @validator("limit")
    def limit_check(cls, v):
        if v < 0 or v > 30:
            raise ValueError("Вы ввели неправильный лимит")