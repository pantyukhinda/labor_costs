from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING

from app.database import Base

if TYPE_CHECKING:
    from app.activity_types.models import ActivityType
    from app.devisions.models import Division
    from app.projects.models import Project


class Organisation(Base):
    __tablename__ = "organisations"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[Optional[str]] = mapped_column(String(255))

    # Relationships
    activity_types: Mapped[list["ActivityType"]] = relationship(
        "ActivityType",
        back_populates="organisation",
    )
    project: Mapped[list["Project"]] = relationship(
        "Project",
        back_populates="organisation",
    )
    division: Mapped[list["Division"]] = relationship(
        "Division",
        back_populates="organisation",
    )
