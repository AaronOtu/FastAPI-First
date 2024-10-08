from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/")
async def read_root():
    return {"message": "App installed successfully"}


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)








