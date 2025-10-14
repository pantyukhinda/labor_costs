from sqlalchemy import BigInteger, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from app.database import Base

# if TYPE_CHECKING:
#     from app.activity_types.models import ActivityType
#     from app.projects.models import Project
#     from app.users.models import User


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="NO ACTION", ondelete="NO ACTION"),
        nullable=False,
    )
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", onupdate="NO ACTION", ondelete="NO ACTION"),
        nullable=False,
    )
    type_of_activity_id: Mapped[int] = mapped_column(
        ForeignKey(
            "activity_types.id",
            onupdate="NO ACTION",
            ondelete="NO ACTION",
        ),
        nullable=False,
    )
    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship(
        back_populates="task",
    )
    project: Mapped["Project"] = relationship(
        back_populates="task",
    )
    activity_type: Mapped["ActivityType"] = relationship(
        back_populates="task",
    )

    def __repr__(self) -> str:
        return (
            f"Task(id={self.id}, user_id={self.user_id}, project_id={self.project_id})"
        )
