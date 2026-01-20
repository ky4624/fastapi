from fastapi import APIRouter,Request
from typing import Optional
from pydantic import BaseModel,Field,validator,EmailStr
import os
response = APIRouter()

    
#函数响应是从下往下先匹配

class user07in(BaseModel):#请求的类
    username:str
    password:str
    email:EmailStr
    fullname:Optional[str] = None

class user07out(BaseModel):#响应的类
    username:str
    email:EmailStr
    fullname:Optional[str] = None

class item(BaseModel):
    name:str
    descrption:Optional[str] = None
    price:float
    tax:float = 10.5
    tags:list[str] = []

items = {
    "foo":{"name":"item1","price":100},
    "baz":{"name":"item2","price":200,"tax":20.5},
    "bar":{"name":"item3","price":300,"descrption":"item3 descrption"},
}

@response.post('/resp',response_model=user07out)#response_model指响应按什么类返回  
async def resp(user:user07in):
    return user

@response.get('/item/{item_id}',response_model=item,response_model_exclude_unset=True)# exclude_unset=True是排除未设置的字段
async def item(item_id:str):
    return items.get(item_id)

@response.get('/item2/{item_id}',response_model=item,response_model_exclude={"name"})# include={"field"}是包含   exclude={"field"}是排除
async def item(item_id:str):
    return items.get(item_id)