from urllib import response
from fastapi import APIRouter

from models.calc_models import CalcPost
from db_config import db

router = APIRouter()

@router.post("/calc")
async def calc_post(body: CalcPost):
    result = 0
    exp_str = ''
    op1 = body.operation1
    val1 = body.value1
    exp = body.expression

    if op1 == "+":
        result = +val1
    elif op1 == "-":
        result = -val1

    exp_str += op1 + str(val1)
    for i in range(len(exp)):
        if exp[i].value == int(exp[i].value):
            exp[i].value = int(exp[i].value)

        exp_str += exp[i].operation + str(exp[i].value)

        if exp[i].operation == "+":
            result += exp[i].value
        elif exp[i].operation == "-":
            result -= exp[i].value
        elif exp[i].operation == "*":
            result *= exp[i].value
        elif exp[i].operation == "/":
            result /= exp[i].value
        else:
            raise ValueError("Ваша операция не является арифметической")

    result = round(result, 3)
    if result == int(result):
        result = int(result)
    await db.create_expression(exp_str, result, "success")

    return f"{exp_str} = {result}"
