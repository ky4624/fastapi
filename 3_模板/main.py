from fastapi import FastAPI
import uvicorn
from apps.urls import modeler
from apps.url2s import modeler2

app = FastAPI()
app.include_router(modeler,prefix='/modeler',tags=['模板'])
app.include_router(modeler2,prefix='/modeler',tags=['模板2'])



if __name__ == '__main__':
    uvicorn.run("main:app",host='127.0.0.1',port=8040,reload=True)

