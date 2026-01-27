from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class TaskBase(BaseModel):
    user_id: int
    project_id: int
    type_of_activity_id: int
    start_time: datetime
    end_time: datetime
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
