# Pydantic схемы
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    user_id: int
    project_id: int
    type_of_activity_id: int
    start_time: datetime
    end_time: datetime
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    user_id: Optional[int] = None
    project_id: Optional[int] = None
    type_of_activity_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    description: Optional[str] = None


class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
