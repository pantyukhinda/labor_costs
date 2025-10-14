from sqlalchemy import BigInteger, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from app.database import Base

# if TYPE_CHECKING:
#     from app.organisations.models import Organisation
#     from app.tasks.models import Task


class ActivityType(Base):
    __tablename__ = "activity_types"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[Optional[str]] = mapped_column(String(255))
    organisation_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
    )
    visible: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    organisation: Mapped[Optional["Organisation"]] = relationship(
        back_populates="activity_type",
    )
    task: Mapped[list["Task"]] = relationship(
        back_populates="activity_type",
    )
