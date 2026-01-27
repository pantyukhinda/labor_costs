from core.dao import BaseDAO

from .models import Project


class ProjectDAO(BaseDAO):
    model = Project
