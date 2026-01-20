from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
modeler2 = APIRouter()
templates = Jinja2Templates(directory='templates')



@modeler2.get('/md2')
async def index(request:Request):
    username = '张三'
    username2 = 'Tom'
    age = 18
    books = ["三国演义","水浒传","西游记","红楼梦"]
    authors = [{"name":"三国演义","author":"罗贯中","bar":85},{"name":"水浒传","author":"施耐庵","bar":80},{"name":"西游记","author":"吴承恩","bar":88},{"name":"红楼梦","author":"曹雪芹","bar":90}]
    pi = 3.14159265
    return templates.TemplateResponse('echarts.html',{
        'request':request,
        'username':username,
        'username2':username2,
        'age':age,
        'books':books,
        'authors':authors,
        'pi':pi})

