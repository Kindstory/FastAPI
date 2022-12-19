from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

chris = FastAPI()

@chris.get('/blog')
def index(limit = 10, published:bool = True, sort:Optional[str] = None):
   
    if published:
        return {'data':f'{limit} published blogs from db'}
    else:
        return {'data':f'{limit} blogs from db'}
    


@chris.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


@chris.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@chris.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@chris.post('/blog')
def create_blog(blog : Blog):
    return {'data': f"Blog is created with title as {blog.title}"}




