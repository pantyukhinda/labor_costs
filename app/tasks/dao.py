from app.models.task import Task
from app.core.dao.base import BaseDAO


class TaskDAO(BaseDAO):
    model = Task
