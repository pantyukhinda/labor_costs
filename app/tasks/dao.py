from core.dao import BaseDAO

from .models import Task


class TaskDAO(BaseDAO):
    model = Task
