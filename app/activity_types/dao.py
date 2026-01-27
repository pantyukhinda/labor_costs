from app.models.activity_type import ActivityType
from app.core.dao.base import BaseDAO


class ActivityTypeDAO(BaseDAO):
    model = ActivityType
