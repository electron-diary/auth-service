from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserRequest:
    user_uuid: str


@dataclass(frozen=True)
class CreateUserRequest:
    user_name: str
    user_contact: str | int


@dataclass(frozen=True)
class DeleteUserRequest:
    user_uuid: str


@dataclass(frozen=True)
class UpdateUserContactRequest:
    user_uuid: str
    user_contact: str | int


@dataclass(frozen=True)
class UpdateUserNameRequest:
    user_uuid: str
    user_name: str