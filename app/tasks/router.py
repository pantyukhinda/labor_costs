from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from dependencies.user import get_current_user
from users.models import User

from .schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
)
from .dao import TaskDAO


router = APIRouter(prefix="/task", tags=["task"])


@router.post("/add", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    """Create new task"""
    new_task = await TaskDAO.add(**task.model_dump())
    return TaskResponse.model_validate(new_task)


@router.get(
    "/all",
    response_model=List[TaskResponse],
    status_code=status.HTTP_201_CREATED,
)
async def get_all_tasks():
    """Get all tasks"""
    all_tasks = await TaskDAO.find_all()
    if not all_tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return [TaskResponse.model_validate(a_type) for a_type in all_tasks]


# TODO: Add handlers for get all tasks of a specific project
@router.get("/tasks_of_current_user")
async def get_current_user_tasks(user: User = Depends(get_current_user)):
    """Get all tasks of a specific user"""

    return await TaskDAO.find_all(user_id=user.id)


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task_by_id(task_id: int):
    """Get task by id"""

    task = await TaskDAO.find_one_or_none(id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="No task found")
    return TaskResponse.model_validate(task)


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Update task"""
    update_a_type = await TaskDAO.update(id=task_id, **task_update.model_dump())
    if not update_a_type:
        raise HTTPException(status_code=404, detail="Task not found")

    return TaskResponse.model_validate(update_a_type)


@router.patch("/{task_id}", response_model=TaskResponse)
async def partial_update_task(task_id: int, task_update: TaskUpdate):
    """Partial update task"""
    update_a_type = await TaskDAO.update(
        id=task_id, **task_update.model_dump(exclude_unset=True)
    )
    if not update_a_type:
        raise HTTPException(status_code=404, detail="Task not found")

    return TaskResponse.model_validate(update_a_type)


@router.delete("/{task_id}", response_model=TaskResponse)
async def delete_task(task_id: int):
    """Delete task"""
    del_task = await TaskDAO.delete(id=task_id)
    if not del_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskResponse.model_validate(del_task)
