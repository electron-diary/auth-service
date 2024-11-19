from typing import Self
from sqlalchemy import UUID, Column, Integer, String

from app.adapters.database.postgres.tables.base import Base


class UserTable(Base):
    __tablename__ = "users"

    uuid = Column("uuid", UUID, primary_key=True)
    first_name = Column("first_name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    middle_name = Column("middle_name", String, nullable=True)
    user_phone = Column("user_phone", Integer, nullable=True, unique=True)
    user_email = Column("user_email", String, nullable=True, unique=True)

    def to_dict(self: Self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}