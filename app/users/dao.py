from app.models.user import User
from app.core.dao.base import BaseDAO


class UserDAO(BaseDAO):
    model = User
