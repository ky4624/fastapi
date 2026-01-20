from fastapi import APIRouter,Form,File,UploadFile
from pydantic import BaseModel,Field,validator
import os
fileUpload = APIRouter()


#函数响应是从下往下先匹配

@fileUpload.post('/file')
async def fileupload(file:bytes = File()):#上传一个文件
    print(f"file:{file}")
    #适合小文件上传
    file = {'file':len(file)}
    return file

@fileUpload.post('/files')
async def fileuploads(files:list[bytes] = File()):#上传多个文件
    print(f"file:{files}")
    #适合小文件上传
    file = {'file':len(files)}
    return file

@fileUpload.post('/file_')
async def fileupload_(file:UploadFile):#上传文件句柄  单个文件上传
    print(f"file:{file}")
    #适合小文件上传
    if not os.path.exists("imgs"):
        os.makedirs("imgs")
    path = os.path.join("imgs",file.filename)
    with open(path,"wb") as f:
        for line in file.file:
            f.write(line)
    return file.filename

@fileUpload.post('/file_s')
async def fileupload_s(files:list[UploadFile]):#上传文件句柄  单个文件上传
    #适合小文件上传
    if not os.path.exists("imgs"):
        os.makedirs("imgs")
    fns = []
    for file in files:
        fns.append(file.filename)
        path = os.path.join("imgs",file.filename)
        with open(path,"wb") as f:
            for line in file.file:
                f.write(line)
    return f"names:{fns}"

