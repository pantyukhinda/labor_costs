from app.models.organization import ActivityType
from app.dao.base import BaseDAO


class ActivityTypeDAO(BaseDAO):
    model = ActivityType
