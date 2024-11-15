from abc import abstractmethod
from typing import Protocol, Self

from app.application.dto.user_dto import UserDto
from app.domain.constants.user_fullname import UserFullName
from app.domain.value_objects.uuid_value_object import UUIDValueObject


class UserQueriesRepository(Protocol):
    @abstractmethod
    async def get_user_by_id(self: Self, uuid: UUIDValueObject) -> UserDto:
        raise NotImplementedError(
            "Method must be implementing be subclasses",
        )


class SearchUserQueriesRepository(Protocol):
    @abstractmethod
    async def search_user_by_name(self: Self, user_fullname: UserFullName) -> UserDto:
        raise NotImplementedError(
            "Method must be implementing be subclasses",
        )
