from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateUserCommand:
    username: str
    phone_number: int

@dataclass(frozen=True)
class UpdateContactsCommand:
    user_id: UUID
    phone_number: int

@dataclass(frozen=True)
class UpdateUsernameCommand:
    user_id: UUID
    username: str

@dataclass(frozen=True)
class DeleteUserCommand:
    user_id: UUID

@dataclass(frozen=True)
class RestoreUserCommand:
    user_id: UUID

