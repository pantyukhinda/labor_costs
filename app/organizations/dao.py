from app.models.organization import Organization
from app.core.dao.base import BaseDAO


class OrganizationDAO(BaseDAO):
    model = Organization
