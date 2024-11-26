from typing import Self
from sqlalchemy import UUID, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...

class UserTable(Base):
    __tablename__ = "users"

    id = Column('id', UUID(as_uuid=True), primary_key=True)
    username = Column('username', String, nullable=False, unique=True)
    email = Column('email', String, nullable=True, unique=True)
    phone_number = Column('phone_number', String, nullable=True, unique=True)
    delete_date = Column('delete_date', DateTime, nullable=True)
    created_date = Column('created_date', DateTime, nullable=False)

    def to_dict(self: Self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}