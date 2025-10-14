from sqlalchemy import BigInteger, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Any, Optional, TYPE_CHECKING

from app.database import Base

if TYPE_CHECKING:
    from app.organisations.models import Organisation
    from app.users.models import User


class Division(Base):
    __tablename__ = "divisions"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    division: Mapped[Optional[Any]] = mapped_column(JSON)
    organisation_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )

    # Relationships
    organisation: Mapped["Organisation"] = relationship(
        back_populates="division",
    )
    user: Mapped[list["User"]] = relationship(
        back_populates="division",
    )
