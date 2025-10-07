from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from app.database import Base

if TYPE_CHECKING:
    from app.devisions.models import Division
    from app.tasks.models import Task


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    last_name: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(255))
    patronymic: Mapped[Optional[str]] = mapped_column(String(255))
    division_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "division.id",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
    )

    # Relationships
    division: Mapped["Division"] = relationship(
        "Division",
        back_populates="user",
    )
    task: Mapped[list["Task"]] = relationship(
        "Task",
        back_populates="user",
    )
