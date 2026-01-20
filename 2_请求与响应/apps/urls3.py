from fastapi import APIRouter
from pydantic import BaseModel,Field,validator
from datetime import date
data = APIRouter()

class User(BaseModel):
    name: str
    age: int = Field(default=0, description="年龄", gt=0, lt=80)#字段约束
    birth: date
    friends: list[str] = []
    
    @validator('name')#校验字段类型
    def name_must_be_yuan(cls, v):
        assert v.isalpha(), "姓名只能包含字母"#判断姓名且是否正常返回
        return v


class Data(BaseModel):
    data: list[User]

#函数响应是从下往下先匹配

@data.post('/data')
async def data_post(data: User):#请求体数据
    return data

@data.post('/data2')
async def data_post2(data: Data):#请求体数据
    return data

