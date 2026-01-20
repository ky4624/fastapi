from fastapi import APIRouter

user = APIRouter()

@user.post("/login")
def shop_login():
    return {"user": "login"}

@user.post("/reg")
def shop_reg():
    return {"user": "reg"}