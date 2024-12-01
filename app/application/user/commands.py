from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_command import BaseCommand


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    username: str
    phone_number: int

@dataclass(frozen=True)
class UpdateContactsCommand(BaseCommand):
    user_id: UUID
    phone_number: int

@dataclass(frozen=True)
class UpdateUsernameCommand(BaseCommand):
    user_id: UUID
    username: str

@dataclass(frozen=True)
class DeleteUserCommand(BaseCommand):
    user_id: UUID

@dataclass(frozen=True)
class RestoreUserCommand(BaseCommand):
    user_id: UUID

