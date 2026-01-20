from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from apps.settings import tortoise_orm
from api.student import student_api


app = FastAPI()
register_tortoise(
    app=app,
    config=tortoise_orm     
)
app.include_router(student_api, prefix="/student", tags=["选课系统的查询所有学生接口"])
#0.执行main.py  启动服务
#1.aerich init -t apps.settings.tortoise_orm   另开窗口执行左边这条命令
#2.aerich init-db 数据库迁移(创建表)
#3.aerich migrate 数据库迁移(更新表) 创建了执行语句
#4.aerich upgrade | aerich downgrade 数据库迁移(更新表)  执行了执行语句增加字段|执行了执行语句删除字段

if __name__ == '__main__':
    uvicorn.run("main:app",host='127.0.0.1',port=8090,reload=True)