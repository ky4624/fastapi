from fastapi import APIRouter
from typing import Union
job = APIRouter()

#函数响应是从下往下先匹配

@job.get('/job/{id}')#大括号写的就是变量 路径参数
async def job_get(kd: Union[str, int], id: int,gj: str = None):#不是路径参数里面的就是查询参数    有默认参数即可以填也可以不填   Union[str, int] 表示kd可以是字符串也可以是整数
    #基于id 和 kd 的查询
    return {"jobName": f"拉钩网", "id": id, "kd": kd, "gj": gj}
