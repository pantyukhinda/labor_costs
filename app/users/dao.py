from core.dao import BaseDAO

from .models import User


class UserDAO(BaseDAO):
    model = User
