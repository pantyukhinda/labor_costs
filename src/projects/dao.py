from app.models.project import Project
from app.core.dao.base import BaseDAO


class ProjectDAO(BaseDAO):
    model = Project
