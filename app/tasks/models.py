from sqlalchemy import (
    Column,
    BigInteger,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True)
    user = Column(
        BigInteger,
        ForeignKey("users.id", onupdate="NO ACTION", ondelete="NO ACTION"),
        nullable=False,
    )
    project = Column(
        BigInteger,
        ForeignKey("projects.id", onupdate="NO ACTION", ondelete="NO ACTION"),
        nullable=False,
    )
    type_of_activity = Column(
        BigInteger,
        ForeignKey("activity_types.id", onupdate="NO ACTION", ondelete="NO ACTION"),
        nullable=False,
    )
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=False)
    description = Column(Text)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    users_rel = relationship("Users", back_populates="tasks")
    projects_rel = relationship("Projects", back_populates="tasks")
    activity_types = relationship("ActivityTypes", back_populates="tasks")
