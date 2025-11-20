from sqlalchemy import BigInteger, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from app.models.base import Base

if TYPE_CHECKING:
    from app.models import Organization
    from app.models import Task


class ActivityType(Base):
    """Represents a table of activity types"""

    name: Mapped[str] = mapped_column(String(255))
    organization_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("organizations.id", onupdate="CASCADE", ondelete="RESTRICT"),
    )
    visible: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    organization: Mapped[Optional["Organization"]] = relationship(
        back_populates="activity_type",
    )
    task: Mapped[list["Task"]] = relationship(
        back_populates="activity_type",
    )
