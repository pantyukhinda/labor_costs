from typing import Any, Optional, TYPE_CHECKING

from sqlalchemy import BigInteger, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from organizations.models import Organization
    from users.models import User


class Division(Base):
    """Represents a table of divisions"""

    division: Mapped[Optional[Any]] = mapped_column(JSON)
    organization_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("organizations.id", onupdate="CASCADE", ondelete="RESTRICT"),
    )

    # Relationships
    organization: Mapped["Organization"] = relationship(
        back_populates="division",
    )
    user: Mapped[list["User"]] = relationship(
        back_populates="division",
    )
