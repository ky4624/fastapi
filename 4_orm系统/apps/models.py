from tortoise import fields
from tortoise.models import Model


class Student(Model):#学生类
    id = fields.IntField(pk=True)#这是主键
    name = fields.CharField(max_length=30,description='姓名')
    pwd = fields.CharField(max_length=30,description='密码')
    age = fields.IntField(description='年龄')
    sex = fields.CharField(max_length=10,description='性别')
    sno = fields.IntField(description='学号')

    #一对多的关系
    clas = fields.ForeignKeyField('models.Clas',related_name='students')#班级类的外键

    #多对多的关系
    courses = fields.ManyToManyField('models.Course',related_name='students')#课程类的外键

class Course(Model):#课程类
    id = fields.IntField(pk=True)#这是主键
    name = fields.CharField(max_length=30,description='课程名称')
    #一对多
    teacher = fields.ForeignKeyField('models.Teacher',related_name='courses')#教师类的外键

class Clas(Model):#班级类
    id = fields.IntField(pk=True)#这是主键
    name = fields.CharField(max_length=30,description='班级名称')
    addr = fields.CharField(max_length=30,description='班级地址',default='')

class Teacher(Model):#教师类
    id = fields.IntField(pk=True)#这是主键
    name = fields.CharField(max_length=30,description='姓名')
    pwd = fields.CharField(max_length=30,description='密码')
    age = fields.IntField(description='年龄')
    sex = fields.CharField(max_length=10,description='性别')
    title = fields.CharField(max_length=30,description='职称')