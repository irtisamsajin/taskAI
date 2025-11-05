from fastapi import FastAPI
from dotenv import load_dotenv
from .Routes import task

load_dotenv()
app=FastAPI()
app.include_router(task.router)

@app.get("/")
def root():
    return {'Reached main'}
