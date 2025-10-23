from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """Base class for all models"""

    __abstract__ = True

    # Generate table name from class name
    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"
