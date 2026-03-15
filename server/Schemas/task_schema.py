from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    title:str
    description: Optional[str] = None
    due_time: Optional[datetime] = None