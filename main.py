from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:

        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool] = None


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'The title of the blog created is {blog.title}'}
