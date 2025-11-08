from datetime import date


from sqlalchemy import func, insert, delete, select, and_, or_
from sqlalchemy.exc import SQLAlchemyError

from app.models.organization import Organization
from app.dao.base import BaseDAO
from app.database import database


class OrganizationDAO(BaseDAO):
    model = Organization
