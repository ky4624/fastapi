from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from apps.urls import user
from apps.urls2 import job
from apps.urls3 import data
from apps.urls4 import form
from apps.urls5 import fileUpload
from apps.urls6 import req
from apps.urls7 import response

import uvicorn

static = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static):
    os.makedirs(static)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(user, prefix="/user", tags=["01 路径参数"])
app.include_router(job, prefix="/job", tags=["02 查询参数"])
app.include_router(data, prefix="/data", tags=["03 请求体数据"])
app.include_router(form, prefix="/form", tags=["04 表单数据"])
app.include_router(fileUpload, prefix="/fileUpload", tags=["05 文件上传"])
app.include_router(req, prefix="/req", tags=["06 requests请求对象"])
app.include_router(response, prefix="/resp", tags=["07 responses响应对象"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
