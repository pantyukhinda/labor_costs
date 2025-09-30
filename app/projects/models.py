from sqlalchemy import BigInteger, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[Optional[str]] = mapped_column(String(255))
    completed: Mapped[Optional[bool]] = mapped_column(Boolean)
    organisation_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
    )

    # Relationships
    organisation: Mapped[Optional["Organisation"]] = relationship(
        back_populates="projects"
    )
    tasks: Mapped[list["Task"]] = relationship(back_populates="project")
