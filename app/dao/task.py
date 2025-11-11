from app.models.task import Task
from app.dao.base import BaseDAO


class TaskDAO(BaseDAO):
    model = Task
