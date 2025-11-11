# Pydantic схемы
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    user_id: Optional[int] = None
    project_id: Optional[int] = None
    type_of_activity_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    description: Optional[str] = None

    class Config:
        from_attributes = True


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
