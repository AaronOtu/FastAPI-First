from fastapi import FastAPI



app = FastAPI()

@app.get('/')
def index():
  return {'data': {'name': 'Aaron'}}

@app.get('/about')
def about():
  return {'data': "I'm a software engineer"}