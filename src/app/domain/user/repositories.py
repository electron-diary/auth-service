from typing import Protocol, Self
from abc import abstractmethod

from src.app.domain.user.entity import UserEntity
from src.app.domain.user.value_objects import UserUUID
from src.app.domain.user.value_objects import UserName
from src.app.domain.user.value_objects import UserContact
from src.app.domain.user.value_objects import UserPassword
from src.app.domain.user.value_objects import UserCreatedAt
from src.app.domain.user.value_objects import UserUpdatedAt
from src.app.domain.user.value_objects import UserStatus


class UserInterface(Protocol):
    @abstractmethod
    async def create_user(
        self: Self,
        user_name: UserName,
        user_contact: UserContact,
        user_password: UserPassword,
        user_status: UserStatus,
        user_created_at: UserCreatedAt,
        user_updated_at: UserUpdatedAt
    ) -> UserUUID:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def get_user_by_uuid(self: Self, user_uuid: UserUUID) -> UserEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def delete_user(self: Self, user_uuid: UserUUID) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def get_user_by_contact(self: Self, user_contact: UserContact) -> UserEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
