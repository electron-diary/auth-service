from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class UserData:
    user_uuid: str
    status: bool


@dataclass(frozen=True)
class TokenData:
    token: str | bytes
    expires_at: datetime