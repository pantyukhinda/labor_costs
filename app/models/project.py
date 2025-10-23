from sqlalchemy import BigInteger, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from app.models.base import Base

if TYPE_CHECKING:
    from app.models import Organization
    from app.models import Task


class Project(Base):
    """Represents a table of projects"""

    name: Mapped[Optional[str]] = mapped_column(String(255))
    completed: Mapped[Optional[bool]] = mapped_column(Boolean)
    organization_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("organizations.id", onupdate="CASCADE", ondelete="RESTRICT"),
    )

    # Relationships
    organization: Mapped[Optional["Organization"]] = relationship(
        back_populates="project",
    )
    task: Mapped[list["Task"]] = relationship(
        back_populates="project",
    )
