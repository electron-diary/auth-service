from typing import Self, Protocol, Any
from abc import abstractmethod

from app.application.base.command_handler import CommandHandler
from app.application.base.event_handler import EventHandler
from app.application.base.query_handler import QueryHandler
from app.application.base.base_command import BaseCommand
from app.application.base.base_query import BaseQuery
from app.domain.base.domain_event import DomainEvent


class CommandMediatorInterface(Protocol):
    @abstractmethod
    def register_command_handler(self: Self, command_type: BaseCommand, handler: CommandHandler) -> None:
        raise NotImplementedError('method must be implemented by subclasses')

    @abstractmethod
    async def process_command(self: Self, command: BaseCommand) -> Any:
        raise NotImplementedError('method must be implemented by subclasses')
    

class QueryMediatorInterface(Protocol):
    @abstractmethod
    def register_query_handler(self: Self, query_type: BaseQuery, handler: QueryHandler) -> None:
        raise NotImplementedError('method must be implemented by subclasses')

    @abstractmethod
    async def process_query(self: Self, query: BaseQuery) -> Any:
        raise NotImplementedError('method must be implemented by subclasses')
    

class EventMediatorInterface(Protocol):
    @abstractmethod
    def register_event_handler(self: Self, event_type: DomainEvent, handler: EventHandler) -> None:
        raise NotImplementedError('method must be implemented by subclasses')

    @abstractmethod
    async def process_events(self: Self, events: list[DomainEvent]) -> None:
        raise NotImplementedError('method must be implemented by subclasses')


class MediatorInterface(EventMediatorInterface, QueryMediatorInterface, CommandMediatorInterface):
    ...
