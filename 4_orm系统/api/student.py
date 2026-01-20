from fastapi import APIRouter
from apps.models import *
from pydantic import BaseModel,validator
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
student_api = APIRouter()


@student_api.get("/")
async def getAllStudent():
    # 异步查询所有学生
    # students = await Student.all()#返回的是Queryset对象 [Student(),Student(),Student()]   查询所有学生
    # for student in students:
    #     print(student.name)

    # 过滤查询
    # students = await Student.filter(name='rain')#返回的是Queryset对象 [Student(),Student()]   查询所有姓名为rain的学生
    # for student in students:
    #     print(student.name)

    # 模糊查询
                                  #(id__range=[1,4])取id为1到4的学生
                                  #(id__in=[2,3])取id为2和3的学生
    # students = await Student.filter(id__gt=2)#返回的是Queryset对象 [Student(),Student()]   查询所有学号大于2的学生
    # for student in students:
    #     print(student.name)

    # values查询
    # students = await Student.filter(id__gt=2).values('name','age')#返回的是Queryset对象 [{'name':'rain','age':18},{'name':'rain','age':18}]   查询所有学号大于2的学生的姓名和年龄
    # for student in students:
    #     print(student)

    # 一对多的查询
    # stu = await Student.get(name='rain')
    # clasname = await stu.clas.values('name')
    # return clasname

    # stus = await Student.all().values('name','clas__name')
    # return stus

    # 多对多的查询
    stus = await Student.all().values('name','courses__name','courses__teacher__name','clas__name')
    return stus

@student_api.get("/index.html")#查询所有学生的姓名和年龄
async def getIndex(request: Request):
    # 异步查询所有学生的姓名和年龄
    students = await Student.all()#返回的是Queryset对象 [{'name':'rain','age':18},{'name':'rain','age':18}]   查询所有学号大于2的学生的姓名和年龄
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("index.html", {"request": request, "students": students})


class studentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    age: int
    sex: str
    clas_id: int
    courses: list[int] = []
    # 验证姓名
    @validator('name')
    def check_name_isalpha(cls, value):
        assert value.isalpha(), '姓名只能包含字母'
        return value

    # 验证学号
    @validator('sno')
    def check_sno(cls, value):
        assert value>1 and value<100, '学号只能在1-100范围内'
        return value

@student_api.post("/")
async def createOneStudent(studentIn: studentIn):
    #插入一个学生到数据库

    #方式1
    # student = Student(
    #     name=studentIn.name,
    #     pwd=studentIn.pwd,
    #     sno=studentIn.sno,
    #     age=studentIn.age,
    #     sex=studentIn.sex,
    #     clas_id=studentIn.clas_id
    # )
    # await student.save()
    # return {"操作": f"添加一个学生"}

    #方式2
    # student = await Student.create(
    #     name=studentIn.name,
    #     pwd=studentIn.pwd,
    #     sno=studentIn.sno,
    #     age=studentIn.age,
    #     sex=studentIn.sex,
    #     clas_id=studentIn.clas_id
    # )
    # return student

    #多对多关联
    student = await Student.create(
        name=studentIn.name,
        pwd=studentIn.pwd,
        sno=studentIn.sno,
        age=studentIn.age,
        sex=studentIn.sex,
        clas_id=studentIn.clas_id
    )
    choose_course = await Course.filter(id__in=studentIn.courses)
    await student.courses.add(*choose_course)
    return student



@student_api.get("/{id}")
async def getOneStudent(id: int):
    #异步查询一个学生
    student = await Student.get(id=id)#返回的是一个Student对象
    return student


@student_api.put("/{id}")
async def updateOneStudent(id: int,studentIn: studentIn):
    #将字典中所有键值对更新
    data = studentIn.dict()
    course= data.pop('courses')#这是多对多的关系 没办法直接修改  先删除
    await Student.filter(id=id).update(**data)
    edit_data = await Student.get(id=id) #获取更新后的学生对象
    choose_course = await Course.filter(id__in=course) #获取选择的课程对象
    await edit_data.courses.clear() #先清空关系表
    await edit_data.courses.add(*choose_course) #再次赋值
    return edit_data
    

@student_api.delete("/{id}")
async def deleteOneStudent(id: int):
    #删除一个学生
    deletesource = await Student.filter(id=id).delete()
    if not deletesource:
        raise HTTPException(status_code=404, detail="学生不存在")
    return {"操作": f"删除id为{id}的学生"}