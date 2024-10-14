from typing import Protocol, Self
from abc import abstractmethod

from src.app.domain.value_objects.user_contact_value_object import UserContact
from src.app.domain.value_objects.user_created_at_value_object import UserCreatedAt
from src.app.domain.value_objects.user_name_value_object import UserName
from src.app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from src.app.domain.entities.user_entities import UserEntity
from src.app.domain.value_objects.user_uuid_value_object import UserUUID


class UserRepositoryInterface(Protocol):
    @abstractmethod
    async def create_user(
        self: Self,
        user_name: UserName,
        user_contact: UserContact,
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
    async def update_user_name(self: Self, user_uuid: UserUUID, user_name: UserName) -> UserName:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def update_user_contact(self: Self, user_uuid: UserUUID, user_contact: UserContact) -> UserContact:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    