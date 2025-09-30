from sqlalchemy import (
    Column,
    BigInteger,
    JSON,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.database import Base


class Divisions(Base):
    __tablename__ = "divisions"

    id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True)
    division = Column(JSON)
    organisation = Column(
        BigInteger,
        ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )

    # Relationships
    organisation_rel = relationship("Organisations", back_populates="divisions")
    users = relationship("Users", back_populates="divisions_rel")
