from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserCommand:
    username: str
    email: str | None
    phone: int | None
