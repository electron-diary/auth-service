from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, UUID as SQLUUID

from src.app.infrastructure.database.postgres.models.declarative import Base


class UserModel(Base):
    __tablename__ = 'users'

    uuid: Mapped[UUID] = mapped_column(SQLUUID, primary_key=True, default=uuid4())
    user_name: Mapped[str] = mapped_column(String(50), nullable=False)
    user_contact: Mapped[str | int] = mapped_column(String(50)| Integer(30), nullable=False, unique=True)
    user_created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    user_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)