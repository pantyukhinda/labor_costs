from core.dao import BaseDAO

from .models import ActivityType


class ActivityTypeDAO(BaseDAO):
    model = ActivityType
