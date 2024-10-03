from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class UserLoginRequest:
    user_contact: str | int
    user_password: str

@dataclass(frozen=True)
class RegisterUserRequest:
    uuid: UUID
    user_name: str
    user_contact: str | int
    user_password: str
    user_ip: str
    user_status: str
    user_refresh_token: str