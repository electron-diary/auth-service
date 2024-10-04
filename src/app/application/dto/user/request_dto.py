from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class CreateUserRequest:
    user_name: str
    user_contact: str | int
    user_password: str

    