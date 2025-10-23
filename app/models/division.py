from sqlalchemy import BigInteger, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Any, Optional, TYPE_CHECKING

from app.models.base import Base

if TYPE_CHECKING:
    from app.models import Organization
    from app.models import User


class Division(Base):
    """Represents a table of divisions"""

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    division: Mapped[Optional[Any]] = mapped_column(JSON)
    organization_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("organizations.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )

    # Relationships
    organization: Mapped["Organization"] = relationship(
        back_populates="division",
    )
    user: Mapped[list["User"]] = relationship(
        back_populates="division",
    )
