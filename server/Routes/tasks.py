from fastapi import APIRouter,Depends,HTTPException
from typing import List
import asyncpg

from server.Queries.task_queries import GET_TASK_BY_ID,CREATE_TASK,GET_TASKS,DELETE_TASK
from ..Schemas.task_schemas import TaskCreate,TaskResponse,TaskRequest
from ..database import get_db_connection

router=APIRouter()

@router.get('/tasks/getTasks',response_model=List[TaskResponse])
async def getTasks(conn: asyncpg.connection=Depends(get_db_connection)):
    rows=await conn.fetch(GET_TASKS)
    return [dict(row) for row in rows]

@router.post('/tasks/getTasksByIds',response_model=List[TaskResponse])
async def getTasksByIds(taskIds: List[int],conn: asyncpg.connection=Depends(get_db_connection)):
    rows=await conn.fetchmany(GET_TASK_BY_ID,[(id,) for id in taskIds])
    if not rows:
        raise HTTPException(status_code=404,detail="Tasks not found")
    return [dict(row) for row in rows]

@router.post('/tasks/createTask',response_model=TaskResponse)
async def createTask(tasks: TaskCreate,conn: asyncpg.connection=Depends(get_db_connection)):
    row=await conn.fetchrow(CREATE_TASK,tasks.title,tasks.description,tasks.due_time)
    return dict(row)

@router.delete('/tasks/deleteTaskById/{taskID}')
async def deleteTaskById(taskID:int,conn: asyncpg.connection=Depends(get_db_connection)):
    row=await conn.fetch(DELETE_TASK,taskID)
    if not row:
        raise HTTPException(status_code=404,detail="Task not found")
    return "Task Deleted"

