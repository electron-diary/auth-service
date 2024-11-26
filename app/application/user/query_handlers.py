from typing import Self

from app.application.base.event_store import EventStoreRepository
from app.application.base.query_handler import QueryHandler
from app.application.user.dto import UserDTO
from app.application.user.queries import GetUserActionsQuery, GetUserByIdQuery, GetUsersQuery
from app.application.user.repositories import UserReaderRepository
from app.domain.base.domain_event import DomainEvent


class GetUserByIdQueryHandler(QueryHandler[GetUserByIdQuery, UserDTO]):
    def __init__(self: Self, user_reader_repository: UserReaderRepository) -> None:
        self.user_reader_repository: UserReaderRepository = user_reader_repository

    async def __call__(self: Self, query: GetUserByIdQuery) -> UserDTO:
        return await self.user_reader_repository.get_user_by_id(user_id=query.user_id)


class GetUserActionsQueryHandler(QueryHandler[GetUserActionsQuery, list[DomainEvent]]):
    def __init__(self: Self, event_store: EventStoreRepository) -> None:
        self.event_store: EventStoreRepository = event_store

    async def __call__(self: Self, query: GetUserActionsQuery) -> list[DomainEvent]:
        return await self.event_store.get_events(id=query.user_id)


class GetUsersQueryHandler(QueryHandler[GetUsersQuery, list[UserDTO]]):
    def __init__(self: Self, user_reader_repository: UserReaderRepository) -> None:
        self.user_reader_repository: UserReaderRepository = user_reader_repository

    async def __call__(self: Self, query: GetUsersQuery) -> list[UserDTO]:
        return await self.user_reader_repository.get_users()
