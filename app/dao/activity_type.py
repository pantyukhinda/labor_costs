from app.models.activity_type import ActivityType
from app.dao.base import BaseDAO


class ActivityTypeDAO(BaseDAO):
    model = ActivityType
