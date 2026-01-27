from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


if TYPE_CHECKING:
    from activity_types.models import ActivityType
    from divisions.models import Division
    from projects.models import Project


class Organization(Base):
    """Represents a table of organizations"""

    name: Mapped[str] = mapped_column(String(255))

    # Relationships
    activity_type: Mapped[list["ActivityType"]] = relationship(
        back_populates="organization",
    )
    project: Mapped[list["Project"]] = relationship(
        back_populates="organization",
    )
    division: Mapped[list["Division"]] = relationship(
        back_populates="organization",
    )
