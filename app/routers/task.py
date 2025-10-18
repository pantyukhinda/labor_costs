from fastapi import APIRouter, Depends, HTTPException, Query

# from sqlalchemy import and_
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# from app.models import Task
# from app.schemes.task import TaskResponse, TaskCreate

# from app.database import async_session_maker

router = APIRouter(prefix="/tasks", tags=["tasks"])


# @router.post("/add", response_model=TaskResponse)
# async def create_task(task: TaskCreate):
#     """Создание новой задачи"""
#     async with async_session_maker() as session:
#         db_task = Task(**task.model_dump())
#         session.add(db_task)
#         await session.commit()
#         await session.refresh(db_task)
#         return db_task


# @router.get("/", response_model=List[TaskResponse])
# async def get_tasks(
#     user_id: Optional[int] = Query(None, description="Фильтр по пользователю"),
#     start_date: Optional[datetime] = Query(
#         None, description="Начальная дата (включительно)"
#     ),
#     end_date: Optional[datetime] = Query(
#         None, description="Конечная дата (включительно)"
#     ),
#     db: Session = Depends(get_db),
# ):
#     """Получение списка задач с фильтрацией по пользователю и дате"""
#     query = db.query(Task)

#     # Фильтр по пользователю
#     if user_id:
#         query = query.filter(Task.user_id == user_id)

#     # Фильтр по дате
#     if start_date:
#         query = query.filter(Task.start_time >= start_date)
#     if end_date:
#         query = query.filter(Task.end_time <= end_date)

#     tasks = query.order_by(Task.created_at.desc()).all()
#     return tasks


# @router.get("/{task_id}", response_model=TaskResponse)
# async def get_task(task_id: int, db: Session = Depends(get_db)):
#     """Получение задачи по ID"""
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return task


# @router.put("/{task_id}", response_model=TaskResponse)
# async def update_task(
#     task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)
# ):
#     """Обновление задачи"""
#     db_task = db.query(Task).filter(Task.id == task_id).first()
#     if not db_task:
#         raise HTTPException(status_code=404, detail="Task not found")

#     update_data = task_update.dict(exclude_unset=True)
#     for field, value in update_data.items():
#         setattr(db_task, field, value)

#     db.commit()
#     db.refresh(db_task)
#     return db_task


# @router.delete("/{task_id}")
# async def delete_task(task_id: int, db: Session = Depends(get_db)):
#     """Удаление задачи"""
#     db_task = db.query(Task).filter(Task.id == task_id).first()
#     if not db_task:
#         raise HTTPException(status_code=404, detail="Task not found")

#     db.delete(db_task)
#     db.commit()
#     return {"message": "Task deleted successfully"}
