from typing import Optional, TYPE_CHECKING

from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from divisions.models import Division
    from tasks.models import Task
    from groups.models import Group, UserGroup


class User(Base):
    """Represents a table of users"""

    last_name: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(255))
    patronymic: Mapped[Optional[str]] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[Optional[str]] = mapped_column(String(255))
    division_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "divisions.id",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
    )

    # Relationships
    division: Mapped["Division"] = relationship(
        back_populates="user",
    )
    task: Mapped[list["Task"]] = relationship(
        back_populates="user",
    )

    group: Mapped[list["Group"]] = relationship(
        secondary="user_group", back_populates="user"
    )
    user_group_links: Mapped[list["UserGroup"]] = relationship(
        back_populates="user",
    )
