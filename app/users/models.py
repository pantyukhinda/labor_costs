from sqlalchemy import (
    Column,
    BigInteger,
    String,
    ForeignKey,
)

from sqlalchemy.orm import relationship
from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True)
    last_name = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    patronymic = Column(String(255))
    division = Column(
        BigInteger,
        ForeignKey("divisions.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )

    # Relationships
    divisions_rel = relationship("Divisions", back_populates="users")
    tasks = relationship("Tasks", back_populates="users")
