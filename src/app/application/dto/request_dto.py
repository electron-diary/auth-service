from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetUserRequest:
    user_uuid: UUID


@dataclass(frozen=True)
class CreateUserRequest:
    user_name: str
    user_contact: str | int


@dataclass(frozen=True)
class DeleteUserRequest:
    user_uuid: UUID


@dataclass(frozen=True)
class UpdateUserContactRequest:
    user_uuid: UUID
    user_contact: str | int


@dataclass(frozen=True)
class UpdateUserNameRequest:
    user_uuid: UUID
    user_name: str


@dataclass(frozen=True)
class AuthentificateUserRequest:
    user_contact: str


@dataclass(frozen=True)
class EditUserStatusRequest:
    user_uuid: UUID
    user_status: bool