from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from fastapi.requests import Request
from fastapi.responses import Response
import time
from settings import config_orm
app = FastAPI()


# register_tortoise(
#     app=app,
#     config=config_orm,
# )

# @app.middleware("http")
# async def middleware2(request: Request, call_next):
#     #请求代码块
#     print("请求代码块2")
#     response = await call_next(request)
#     #响应代码块
#     print("响应代码块2")
#     return response

# @app.middleware("http")
# async def middleware1(request: Request, call_next):
#     #请求代码块
#     print("请求代码块1")
#     # if request.client.host in ['127.0.0.1', '127.0.2.3']:
#     #     print('请求来自127.0.1.1或127.0.2.3')
#     #     return Response(status_code=403, content='Forbidden')
    
#     # if request.url.path == '/user':
#     #     print('请求路径为/user')
#     #     return Response(status_code=403, content='Forbidden')

#     start_time = time.time()
#     time.sleep(3)
#     response = await call_next(request)
#     #响应代码块
#     print("响应代码块1")
#     end_time = time.time()
#     response.headers['X-Process-Time'] = str(end_time - start_time)
#     return response

# @app.middleware("http")
# async def myCORSmiddleware(request: Request, call_next):#函数名称自己定义  自己写CORS中间件
#     #请求代码块
#     print("请求代码块3")
#     response = await call_next(request)
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
#     #响应代码块
#     print("响应代码块3")
#     return response

app.add_middleware( #FASTAPI 提供的CORS中间件      CORS就是特殊的中间件，用来处理跨域请求
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/user")
async def read_root(req:Request):
    templates = Jinja2Templates(directory="templates")
    templates.TemplateResponse("index.html", {"request": req})
    return {"message": "wang"}

# @app.get("/item/{id}")
# def read_item(id: int):
#     print(f'getitem函数执行，id={id}')
#     return {"item_id": id}



if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8020, reload=True)