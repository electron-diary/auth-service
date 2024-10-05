from dataclasses import dataclass


@dataclass(frozen=True)
class LoginUserDto:
    contact: str | int
    password: str

@dataclass(frozen=True)
class RegisterUserDto:
    user_name: str
    user_contact: str
    user_password: str