from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from app.database import Base


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
        back_populates="organisation"
    )
    projects: Mapped[list["Project"]] = relationship(back_populates="organisation")
    divisions: Mapped[list["Division"]] = relationship(back_populates="organisation")
