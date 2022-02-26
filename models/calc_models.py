from typing import Optional
from pydantic import BaseModel, validator

from db_config import db


class Expression(BaseModel):
    operation : str
    value : float


class CalcPost(BaseModel):
    operation1 : str
    value1 : float
    expression : Optional[list[Expression]] = []

    @validator("operation1")
    def op1_plus_or_minus(cls, op):
        if op not in ["+", "-"]:
            raise ValueError("В начале выражения стоит не + или -")
        return op

    @validator("value1")
    def val_negative(cls, v):
        if v < 0:
            raise ValueError("Вы ввели отрицательно число")
        if v == int(v):
            return int(v)
        return v

    @validator("expression")
    def expression_op_val(cls, v):
        for i in range(len(v)):
            if v[i].operation not in ["+", "-", "/", "*"]:
                raise ValueError("Введена некоректная арифметическая операция")
            elif v[i].value < 0:
                raise ValueError("Вы ввели отрицательное число")
            
            if v[i].value == int(v[i].value):
                v[i].value == int(v[i].value)
        return v

class CalcResponse(BaseModel):
    operation : str
    result : float
    status : str
