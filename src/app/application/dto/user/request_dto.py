from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserRequest:
    user_name: str
    user_contact: str | int

