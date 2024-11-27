from typing import Self

from sqlalchemy import UUID, Column, Integer, String, JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...

class Events(Base):
    __tablename__ = "events"
    sequence_id = Column("sequence_id", Integer, primary_key=True, autoincrement=True)
    agregate_id = Column("agregate_id", UUID(as_uuid=True), nullable=False)
    agregate_type = Column("agregate_type", String, nullable=False)
    event_type = Column("event_type", String, nullable=False)
    event_data = Column("event_data", JSON, nullable=False)
    
    def to_dict(self: Self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}