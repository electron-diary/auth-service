from typing import Self, Protocol
from abc import abstractmethod

from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.domain.base.base_event import BaseDomainEvent

class UserProjectionsRepository(Protocol):
    @abstractmethod
    async def create_user(self: Self, event: CreateUserEvent) -> None:
        msg = "Method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
    @abstractmethod
    async def update_user_fullname(self: Self, event: UpdateUserFullNameEvent) -> None:
        msg = "Method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
    
    @abstractmethod
    async def update_user_contact(self: Self, event: UpdateUserContactEvent) -> None:
        msg = "Method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
    
    @abstractmethod
    async def delete_user(self: Self, event: DeleteUserEvent) -> None:
        msg = "Method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )