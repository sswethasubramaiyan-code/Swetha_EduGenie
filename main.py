from fastapi import FastAPI,Request,Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from qna import answer_question
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations
app=FastAPI(title='EduGenie')
app.mount('/static',StaticFiles(directory='static'),name='static')
templates=Jinja2Templates(directory='templates')
@app.get('/',response_class=HTMLResponse)
async def home(request:Request): return templates.TemplateResponse('index.html',{'request':request})
@app.get('/qa')
async def qa(question:str=Query(...)): return {'answer':answer_question(question)}
@app.post('/explain/')
async def explain(request:Request): d=await request.json(); return {'topic':d.get('topic'),'explanation':explain_topic(d.get('topic',''))}
@app.post('/summarize/')
async def summarize(request:Request): d=await request.json(); return {'summary':summarize_text(d.get('text',''))}
@app.post('/quiz')
async def quiz(request:Request): d=await request.json(); return {'quiz':generate_quiz(d.get('text',''))}
@app.get('/learn/recommendations')
async def learn(topic:str=Query(...)): return {'recommendation':get_learning_recommendations(topic)}
