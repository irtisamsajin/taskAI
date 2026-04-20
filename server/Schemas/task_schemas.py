from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime

class TaskCreate(BaseModel):
    title:str
    description: Optional[str] = None
    due_time: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title:str
    description: str | None
    due_time: datetime | None
    created_at: datetime | None

class TaskRequest(BaseModel):
    id: List[int]