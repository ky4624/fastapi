from fastapi import APIRouter

user = APIRouter()

#函数响应是从下往下先匹配

@user.get('/user/1')#大括号写的就是变量 路径参数
def user_get():#参数名要和大括号里的变量名一致
    #id = 1
    return {"userid": f"root"}

@user.get('/user/{userid}')#大括号写的就是变量 路径参数
def user_get(userid: int):#参数名要和大括号里的变量名一致
    #id = 1
    return {"userid": f"{userid}"}

@user.get('/artics/{articsid}')#大括号写的就是变量 路径参数
def artics_get(articsid: int):#参数名要和大括号里的变量名一致
    #id = 1
    return {"articsid": f"{articsid}"}
