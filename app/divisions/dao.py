from core.dao import BaseDAO

from .models import Division


class DivisionDAO(BaseDAO):
    model = Division
