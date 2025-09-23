from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Text, func, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
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
    description = Column(Text, nullable=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    # Связи с другими моделями
    user_rel = relationship("User", back_populates="tasks")
    project_rel = relationship("Project", back_populates="tasks")
    activity_type_rel = relationship("ActivityType", back_populates="tasks")

    # Индексы для улучшения производительности
    __table_args__ = (
        Index("ix_tasks_user", "user"),
        Index("ix_tasks_project", "project"),
        Index("ix_tasks_activity_type", "type_of_activity"),
        Index("ix_tasks_start_time", "start_time"),
        Index("ix_tasks_created_at", "created_at"),
    )

    def __repr__(self):
        return f"<Task(id={self.id}, user={self.user}, project={self.project}, start={self.start_time})>"

    @property
    def duration(self):
        """Вычисляет продолжительность задачи в секундах"""
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return None

    @property
    def duration_hours(self):
        """Продолжительность в часах с округлением до 2 знаков"""
        duration = self.duration
        if duration:
            return round(duration / 3600, 2)
        return None
