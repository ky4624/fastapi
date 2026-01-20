from fastapi import APIRouter,Request
from pydantic import BaseModel,Field,validator
import os
req = APIRouter()


#函数响应是从下往下先匹配

@req.post('/req')
async def req_(request:Request):
    req = {
        "url":str(request.url),#url
        "clientIP":request.client.host,#客户端IP地址
        "请求宿主":request.headers.get("user-agent"),#请求宿主
        "cookie":request.cookies,#cookie
    }
    return req

