from app.models.project import Project
from app.dao.base import BaseDAO


class ProjectDAO(BaseDAO):
    model = Project
