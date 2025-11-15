from app.models.user import User
from app.dao.base import BaseDAO


class UserDAO(BaseDAO):
    model = User
