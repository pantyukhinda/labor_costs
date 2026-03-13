from typing import Optional, TYPE_CHECKING

from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from organizations.models import Organization
    from users.models import User


class Group(Base):
    """Represents a table of groups"""

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    organization_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "organizations.id",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        ),
    )

    # Relationships
    organization: Mapped["Organization"] = relationship(
        back_populates="group",
    )

    user: Mapped[list["User"]] = relationship(
        secondary="user_group",
        back_populates="group",
    )


class UserGroup(Base):
    """
    User and group relationship model (intermediate table).
    Represents a table of user_group.
    """

    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(
            "users.id",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        )
    )
    group_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(
            "groups.id",
            onupdate="CASCADE",
            ondelete="RESTRICT",
        )
    )

    # Relationships
    user: Mapped[Optional["User"]] = relationship(
        back_populates="user_group_link",
    )
    group: Mapped[Optional["Group"]] = relationship(
        back_populates="user_group_link",
    )
