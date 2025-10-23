from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
)
from sqlalchemy import BigInteger
import re


class Base(DeclarativeBase):
    """Base class for all models"""

    __abstract__ = True

    # Generate table name from class name
    @declared_attr.directive
    def __tablename__(self) -> str:
        table_name = re.sub(r"(?<!^)(?=[A-Z])", "_", self.__name__).lower()
        return f"{table_name}s"

    # TODO: Исправить. В таблицах, созданных при помощи этого базового класса, поле id идет последним.
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
