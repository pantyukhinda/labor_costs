from app.models.organization import Organization
from app.dao.base import BaseDAO


class OrganizationDAO(BaseDAO):
    model = Organization
