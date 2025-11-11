from app.models.division import Division
from app.dao.base import BaseDAO


class DivisionDAO(BaseDAO):
    model = Division
