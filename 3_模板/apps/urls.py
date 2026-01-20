from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
modeler = APIRouter()
templates = Jinja2Templates(directory='templates')



@modeler.get('/md')
async def index(request:Request):
    username = '张三'
    username2 = 'Tom'
    age = 18
    books = ["三国演义","水浒传","西游记","红楼梦"]
    authors = {'三国演义':'罗贯中','水浒传':'施耐庵','西游记':'吴承恩','红楼梦':'曹雪芹'}
    pi = 3.14159265
    return templates.TemplateResponse('index.html',{
        'request':request,
        'username':username,
        'username2':username2,
        'age':age,
        'books':books,
        'authors':authors,
        'pi':pi})

