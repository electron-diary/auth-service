from abc import abstractmethod
from typing import Any, Protocol, Self

from app.application.base.base_command import BaseCommand
from app.application.base.base_query import BaseQuery
from app.application.base.command_handler import CommandHandler
from app.application.base.event_handler import EventHandler
from app.application.base.query_handler import QueryHandler
from app.domain.base.domain_event import DomainEvent


class MediatorInterface(Protocol):
    """
    Defines a protocol for mediator pattern implementation that handles commands, events, and queries.
    The mediator acts as a central hub that coordinates communication between different components
    of the application, promoting loose coupling between objects.
    """

    @abstractmethod
    def register_command_handler(self: Self, command_type: BaseCommand, handler: CommandHandler[BaseCommand, Any]) -> None:
        """
        Registers a handler for a specific command type.

        Args:
            command_type: The type of command to be handled
            handler: The handler implementation that will process the command
        """
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    def register_event_handler(self: Self, event_type: DomainEvent, handler: EventHandler[DomainEvent]) -> None:
        """
        Registers a handler for a specific domain event type.

        Args:
            event_type: The type of domain event to be handled
            handler: The handler implementation that will process the event
        """
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    def register_query_handler(self: Self, query_type: BaseQuery, handler: QueryHandler[BaseQuery, Any]) -> None:
        """
        Registers a handler for a specific query type.

        Args:
            query_type: The type of query to be handled
            handler: The handler implementation that will process the query
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def process_command(self: Self, command: BaseCommand) -> Any:
        """
        Processes a command by routing it to its registered handler.

        Args:
            command: The command to be processed

        Returns:
            Any: The result of the command processing
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def process_events(self: Self, events: list[DomainEvent]) -> None:
        """
        Processes a list of domain events by routing each to their respective handlers.

        Args:
            events: List of domain events to be processed
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def process_query(self: Self, query: BaseQuery) -> Any:
        """
        Processes a query by routing it to its registered handler.

        Args:
            query: The query to be processed

        Returns:
            Any: The result of the query processing
        """
        raise NotImplementedError("method must be implemented by subclasses")
