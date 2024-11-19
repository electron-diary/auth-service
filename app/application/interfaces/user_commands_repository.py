from abc import abstractmethod
from typing import Protocol, Self

from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.uuid_value_object import UUIDValueObject


class UserCommandsRepository(Protocol):
    @abstractmethod
    async def create_user(self: Self, user: UserDomainEntity) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )

    @abstractmethod
    async def update_user_fullname(self: Self, user: UserDomainEntity) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )

    @abstractmethod
    async def update_user_contact(self: Self, user: UserDomainEntity) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )

    @abstractmethod
    async def delete_user(self: Self, user_uuid: UUIDValueObject) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
