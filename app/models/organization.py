from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from app.models.base import Base


if TYPE_CHECKING:
    from app.models import Activity_Type
    from app.models import Division
    from app.models import Project


class Organization(Base):
    """Represents a table of organizations"""

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[Optional[str]] = mapped_column(String(255))

    # Relationships
    activity_type: Mapped[list["Activity_Type"]] = relationship(
        back_populates="organization",
    )
    project: Mapped[list["Project"]] = relationship(
        back_populates="organization",
    )
    division: Mapped[list["Division"]] = relationship(
        back_populates="organization",
    )
