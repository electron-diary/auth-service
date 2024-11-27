from typing import Self

from sqlalchemy import UUID, Column, Boolean, String, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...

class UserTable(Base):
    __tablename__ = "users"

    id = Column("id", UUID(as_uuid=True), primary_key=True)
    username = Column("username", String, nullable=False, unique=True)
    email = Column("email", String, nullable=True, unique=True)
    phone_number = Column("phone_number", Integer, nullable=True, unique=True)
    is_deleted = Column("is_deleted", Boolean, nullable=False, default=False)

    def to_dict(self: Self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
