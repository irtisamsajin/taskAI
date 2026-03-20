from fastapi import APIRouter,Depends,HTTPException
from typing import List
import asyncpg
import os

from server.Queries.task_queries import GET_TASKS_BY_ID,CREATE_TASK,GET_TASKS
from ..Schemas.task_schemas import TaskCreate,TaskResponse,TaskRequest
from ..database import get_db_connection

router=APIRouter()

@router.get('/tasks/{task_id}',response_model=TaskResponse)
async def get_task(task_id:int,conn: asyncpg.connection=Depends(get_db_connection)):
    row=await conn.fetchrow(GET_TASKS_BY_ID,task_id)
    if not row:
        raise HTTPException(status_code=404,detail="Task Not Found")
    return dict(row)

@router.get('/tasks/',response_model=List[TaskResponse])
async def get_tasks(conn: asyncpg.connection=Depends(get_db_connection)):
    rows=await conn.fetch(GET_TASKS)
    return [dict(row) for row in rows]

@router.post('/tasks',response_model=TaskResponse)
async def create_task(tasks: TaskCreate,conn: asyncpg.connection=Depends(get_db_connection)):
    row=await conn.fetchrow(CREATE_TASK,tasks.title,tasks.description,tasks.due_time)

    return dict(row)