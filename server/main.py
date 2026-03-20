from fastapi import FastAPI
from dotenv import load_dotenv

from .Routes import tasks
from .database import lifespan

load_dotenv()

app=FastAPI(lifespan=lifespan)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {'Reached main'}
