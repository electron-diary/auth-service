from typing import Self

from sqlalchemy import UUID, BigInteger, Boolean, Column, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


class UserTable(Base):
    __tablename__ = "users"

    id = Column("id", UUID, unique=True, primary_key=True)
    username = Column("username", String, nullable=False)
    phone_number = Column("phone_number", BigInteger, nullable=False, unique=True)
    is_deleted = Column("is_deleted", Boolean, nullable=False, default=0)

    def to_dict(self: Self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
