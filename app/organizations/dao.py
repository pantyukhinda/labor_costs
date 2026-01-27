from core.dao import BaseDAO

from .models import Organization


class OrganizationDAO(BaseDAO):
    model = Organization
