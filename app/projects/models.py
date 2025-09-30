from sqlalchemy import (
    Boolean,
    Column,
    BigInteger,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.database import Base


class Projects(Base):
    __tablename__ = "projects"

    id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(255))
    completed = Column(Boolean)
    organisation = Column(
        BigInteger,
        ForeignKey("organisations.id", onupdate="CASCADE", ondelete="RESTRICT"),
    )

    # Relationships
    organisations_rel = relationship("Organisations", back_populates="projects")
    tasks = relationship("Tasks", back_populates="projects")
