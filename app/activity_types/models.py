from sqlalchemy import (
    Boolean,
    Column,
    BigInteger,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.database import Base


class ActivityTypes(Base):
    __tablename__ = "activity_types"

    id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(255))
    organisation = Column(
        BigInteger,
        ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
    )
    visible = Column(Boolean, default=True)

    # Relationships
    organisations_rel = relationship("Organisations", back_populates="activity_types")
    tasks = relationship("Tasks", back_populates="activity_types")
