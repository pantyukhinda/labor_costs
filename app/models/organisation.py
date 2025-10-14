from datetime import datetime
from sqlalchemy import (
    JSON,
    BigInteger,
    Boolean,
    DateTime,
    ForeignKey,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Any, Optional, TYPE_CHECKING

from app.database import Base


# if TYPE_CHECKING:
#     from app.activity_types.models import ActivityType
#     from app.divisions.models import Division
#     from app.projects.models import Project


# class Project(Base):
#     __tablename__ = "projects"

#     id: Mapped[int] = mapped_column(
#         BigInteger,
#         primary_key=True,
#         autoincrement=True,
#     )
#     name: Mapped[Optional[str]] = mapped_column(String(255))
#     completed: Mapped[Optional[bool]] = mapped_column(Boolean)
#     organisation_id: Mapped[Optional[int]] = mapped_column(
#         BigInteger,
#         ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
#     )

#     # Relationships
#     organisation: Mapped[Optional["Organisation"]] = relationship(
#         back_populates="project",
#     )
#     task: Mapped[list["Task"]] = relationship(
#         back_populates="project",
#     )


# class Division(Base):
#     __tablename__ = "divisions"

#     id: Mapped[int] = mapped_column(
#         BigInteger,
#         primary_key=True,
#         autoincrement=True,
#     )
#     division: Mapped[Optional[Any]] = mapped_column(JSON)
#     organisation_id: Mapped[int] = mapped_column(
#         BigInteger,
#         ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
#         nullable=False,
#     )

#     # Relationships
#     organisation: Mapped["Organisation"] = relationship(
#         back_populates="division",
#     )
#     user: Mapped[list["User"]] = relationship(
#         back_populates="division",
#     )


# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     last_name: Mapped[str] = mapped_column(String(255))
#     first_name: Mapped[str] = mapped_column(String(255))
#     patronymic: Mapped[Optional[str]] = mapped_column(String(255))
#     division_id: Mapped[int] = mapped_column(
#         BigInteger,
#         ForeignKey(
#             "divisions.id",
#             onupdate="CASCADE",
#             ondelete="RESTRICT",
#         ),
#     )

#     # Relationships
#     division: Mapped["Division"] = relationship(
#         back_populates="user",
#     )
#     task: Mapped[list["Task"]] = relationship(
#         back_populates="user",
#     )


# class Task(Base):
#     __tablename__ = "tasks"

#     id: Mapped[int] = mapped_column(
#         BigInteger,
#         primary_key=True,
#         autoincrement=True,
#     )
#     user_id: Mapped[int] = mapped_column(
#         ForeignKey("users.id", onupdate="NO ACTION", ondelete="NO ACTION"),
#         nullable=False,
#     )
#     project_id: Mapped[int] = mapped_column(
#         ForeignKey("projects.id", onupdate="NO ACTION", ondelete="NO ACTION"),
#         nullable=False,
#     )
#     type_of_activity_id: Mapped[int] = mapped_column(
#         ForeignKey(
#             "activity_types.id",
#             onupdate="NO ACTION",
#             ondelete="NO ACTION",
#         ),
#         nullable=False,
#     )
#     start_time: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), nullable=False
#     )
#     end_time: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         nullable=False,
#     )
#     description: Mapped[Optional[str]] = mapped_column(Text)
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now(), nullable=False
#     )

#     # Relationships
#     user: Mapped["User"] = relationship(
#         back_populates="task",
#     )
#     project: Mapped["Project"] = relationship(
#         back_populates="task",
#     )
#     activity_type: Mapped["ActivityType"] = relationship(
#         back_populates="task",
#     )

#     def __repr__(self) -> str:
#         return (
#             f"Task(id={self.id}, user_id={self.user_id}, project_id={self.project_id})"
#         )


# class ActivityType(Base):
#     __tablename__ = "activity_types"

#     id: Mapped[int] = mapped_column(
#         BigInteger,
#         primary_key=True,
#         autoincrement=True,
#     )
#     name: Mapped[Optional[str]] = mapped_column(String(255))
#     organisation_id: Mapped[Optional[int]] = mapped_column(
#         BigInteger,
#         ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
#     )
#     visible: Mapped[bool] = mapped_column(Boolean, default=True)

#     # Relationships
#     organisation: Mapped[Optional["Organisation"]] = relationship(
#         back_populates="activity_type",
#     )
#     task: Mapped[list["Task"]] = relationship(
#         back_populates="activity_type",
#     )


class Organisation(Base):
    __tablename__ = "organisations"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[Optional[str]] = mapped_column(String(255))

    # Relationships
    activity_type: Mapped[list["ActivityType"]] = relationship(
        back_populates="organisation",
    )
    project: Mapped[list["Project"]] = relationship(
        back_populates="organisation",
    )
    division: Mapped[list["Division"]] = relationship(
        back_populates="organisation",
    )
