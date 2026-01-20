from fastapi import APIRouter,Form
from pydantic import BaseModel,Field,validator
from datetime import date
form = APIRouter()


#函数响应是从下往下先匹配

@form.post('/regin')
async def data_post(username:str = Form(),password:str = Form()):#没有加form就是查询参数  否则就是form解析下的一个变量
    print(f"username:{username},password:{password}")
    #注册实现数据库的一个添加操作
    form_data = {'username':username,'password':password}
    return form_data

