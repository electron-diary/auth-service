from abc import abstractmethod
from typing import Any, Protocol, Self

from app.application.base.base_command import BaseCommand
from app.application.base.base_query import BaseQuery
from app.application.base.command_handler import CommandHandler
from app.application.base.event_handler import EventHandler
from app.application.base.query_handler import QueryHandler
from app.domain.base.domain_event import DomainEvent


class CommandMediatorInterface(Protocol):
    """
    Protocol defining the interface for command mediation.
    Handles registration and processing of command handlers.

    This interface is part of the Mediator pattern implementation,
    specifically focused on command handling in CQRS architecture.
    """

    @abstractmethod
    def register_command_handler(self: Self, command_type: BaseCommand, handler: CommandHandler) -> None:
        """
        Registers a handler for a specific command type.

        Args:
            command_type: Type of command to be handled
            handler: Handler implementation for the command
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def process_command(self: Self, command: BaseCommand) -> Any:
        """
        Processes a command by routing it to its registered handler.

        Args:
            command: Command to be processed
        Returns:
            Any: Result of command processing
        """
        raise NotImplementedError("method must be implemented by subclasses")


class QueryMediatorInterface(Protocol):
    """
    Protocol defining the interface for query mediation.
    Handles registration and processing of query handlers.

    This interface supports the query side of CQRS pattern,
    managing read operations in the system.
    """

    @abstractmethod
    def register_query_handler(self: Self, query_type: BaseQuery, handler: QueryHandler) -> None:
        """
        Registers a handler for a specific query type.

        Args:
            query_type: Type of query to be handled
            handler: Handler implementation for the query
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def process_query(self: Self, query: BaseQuery) -> Any:
        """
        Processes a query by routing it to its registered handler.

        Args:
            query: Query to be processed
        Returns:
            Any: Result of query processing
        """
        raise NotImplementedError("method must be implemented by subclasses")


class EventMediatorInterface(Protocol):
    """
    Protocol defining the interface for event mediation.
    Handles registration and processing of event handlers.

    This interface supports event-driven architecture by managing
    domain event handling and distribution.
    """

    @abstractmethod
    def register_event_handler(self: Self, event_type: DomainEvent, handler: EventHandler) -> None:
        """
        Registers a handler for a specific event type.

        Args:
            event_type: Type of event to be handled
            handler: Handler implementation for the event
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def process_events(self: Self, events: list[DomainEvent]) -> None:
        """
        Processes a list of domain events by routing them to their handlers.

        Args:
            events: List of events to be processed
        """
        raise NotImplementedError("method must be implemented by subclasses")


class MediatorInterface(EventMediatorInterface, QueryMediatorInterface, CommandMediatorInterface):
    """
    Comprehensive mediator interface combining event, query, and command handling.
    
    This interface provides a complete mediation layer for the application,
    implementing the Mediator pattern and supporting CQRS architecture.
    Inherits from all specific mediator interfaces to provide a unified
    point of interaction for the application.
    """

