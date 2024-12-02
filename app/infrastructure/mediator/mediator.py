from typing import Self, Any

from app.application.base.base_mediator import MediatorInterface
from app.application.base.base_query import BaseQuery
from app.application.base.query_handler import QueryHandler
from app.application.base.command_handler import CommandHandler
from app.application.base.base_command import BaseCommand
from app.application.base.event_handler import EventHandler
from app.domain.base.domain_event import DomainEvent


class ConcreteMediator(MediatorInterface):
    """
    Concrete implementation of the Mediator interface that coordinates communication
    between different components of the application using the mediator pattern.
    
    This mediator handles three types of messages:
    - Commands: Operations that change the system state
    - Queries: Operations that retrieve data without changing state
    - Events: Notifications of changes that have occurred in the system
    """

    def __init__(self: Self) -> None:
        """
        Initialize the mediator with empty handler registries for commands,
        queries, and events.
        """
        self.query_handlers: dict[BaseQuery, QueryHandler] = {}
        self.command_handlers: dict[BaseCommand, CommandHandler] = {}
        self.event_handlers: dict[DomainEvent, EventHandler] = {}

    def register_event_handler(self: Self, event: DomainEvent, handler: EventHandler) -> None:
        """
        Register a handler for a specific event type.

        Args:
            event: The domain event type to be handled
            handler: The event handler implementation
        """
        self.event_handlers[event] = handler

    def register_command_handler(self: Self, command: BaseCommand, handler: CommandHandler) -> None:
        """
        Register a handler for a specific command type.

        Args:
            command: The command type to be handled
            handler: The command handler implementation
        """
        self.command_handlers[command] = handler

    def register_query_handler(self: Self, query: BaseQuery, handler: QueryHandler) -> None:
        """
        Register a handler for a specific query type.

        Args:
            query: The query type to be handled
            handler: The query handler implementation
        """
        self.query_handlers[query] = handler

    async def process_command(self: Self, command: BaseCommand) -> Any:
        """
        Process a command by finding and executing its registered handler.

        Args:
            command: The command to be processed

        Returns:
            Any: The result of the command processing

        Raises:
            ValueError: If no handler is registered for the given command type
        """
        handler: CommandHandler = self.command_handlers.get(command)
        if not handler:
            raise ValueError(f"No handler registered for command {command}")
        return await handler(command)
    
    async def process_query(self: Self, query: BaseQuery) -> Any:
        """
        Process a query by finding and executing its registered handler.

        Args:
            query: The query to be processed

        Returns:
            Any: The result of the query processing

        Raises:
            ValueError: If no handler is registered for the given query type
        """
        handler: QueryHandler = self.self.query_handlers.get(query)
        if not handler:
            raise ValueError(f"No handler registered for query {query}")
        return await handler(query)
    
    async def process_events(self: Self, events: list[DomainEvent]) -> None:
        """
        Process a list of domain events by executing their registered handlers.

        Args:
            events: List of domain events to be processed

        Raises:
            ValueError: If no handler is registered for any of the event types
        """
        for event in events:
            handler: EventHandler = self.event_handlers.get(event) 
            if not handler:
                raise ValueError(f"No handler registered for event {event}")
            await handler(event)
