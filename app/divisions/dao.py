from app.models.division import Division
from app.core.dao.base import BaseDAO


class DivisionDAO(BaseDAO):
    model = Division
