from fastapi import FastAPI
from dotenv import load_dotenv

from .Routes import task
from database import lifespan

load_dotenv()

app=FastAPI(lifespan=lifespan)
app.include_router(task.router)

@app.get("/")
def root():
    return {'Reached main'}
