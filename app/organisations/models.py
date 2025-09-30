from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    BigInteger,
    String,
    Text,
    DateTime,
    JSON,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Organisations(Base):
    __tablename__ = "organisations"

    id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(255))

    # Relationships
    activity_types = relationship("ActivityTypes", back_populates="organisations_rel")
    projects = relationship("Projects", back_populates="organisations_rel")
    divisions = relationship("Divisions", back_populates="organisations_rel")
