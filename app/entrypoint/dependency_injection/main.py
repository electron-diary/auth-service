"""
Dependency Injection Configuration Module

This module configures dependency injection containers for both FastAPI and FastStream
applications using the Dishka framework. It sets up different providers for database
connections, event buses, and various handlers.

Imports:
    - AsyncContainer, make_async_container: Core Dishka DI components
    - setup_dishka_fastapi: Dishka integration for FastAPI
    - setup_dishka_faststream: Dishka integration for FastStream
    - FastAPI: Main FastAPI application class
    - FastStream: Main FastStream application class
    - Various providers from local modules
"""
from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka as setup_dishka_fastapi
from dishka.integrations.faststream import setup_dishka as setup_dishka_faststream
from fastapi import FastAPI
from faststream import FastStream

from app.entrypoint.dependency_injection.provide_adapters import (
    GlobalEventBusProvider,
    LocalEventBusProvider,
    MongodbProvider,
    SqlalchemyProvider,
)
from app.entrypoint.dependency_injection.provide_handlers import (
    CommandHandlersProvider,
    EventHandlersProvider,
    QueryHandlersProvider,
)


def fastapi_container() -> AsyncContainer:
    """
    Creates and configures a dependency injection container for FastAPI application.
    
    This container includes all necessary providers for the REST API functionality:
    - MongoDB connection for document storage
    - SQLAlchemy for relational database operations
    - Global event bus for system-wide event publishing
    - Command handlers for processing business commands
    - Query handlers for handling data queries
    - Local event bus for application-specific events
    
    Returns:
        AsyncContainer: Configured dependency injection container for FastAPI
    
    Example:
        ```python
        container = fastapi_container()
        app = FastAPI()
        setup_di_fastapi(app)
        ```
    """
    container: AsyncContainer = make_async_container(
        MongodbProvider(),
        SqlalchemyProvider(),
        GlobalEventBusProvider(),
        CommandHandlersProvider(),
        QueryHandlersProvider(),
        LocalEventBusProvider(),
    )
    return container

def faststream_container() -> AsyncContainer:
    """
    Creates and configures a dependency injection container for FastStream application.
    
    This container includes providers specifically needed for event processing:
    - MongoDB connection for event storage
    - Local event bus for handling internal events
    - Event handlers for processing various system events
    
    Returns:
        AsyncContainer: Configured dependency injection container for FastStream
    
    Example:
        ```python
               container = faststream_container()
        app = FastStream()
        setup_di_faststream(app)
        ```
    """
    container: AsyncContainer = make_async_container(
        MongodbProvider(),
        LocalEventBusProvider(),
        EventHandlersProvider(),
    )
    return container

def setup_di_faststream(app: FastStream) -> None:
    """
    Configures dependency injection for a FastStream application.
    
    Args:
        app (FastStream): The FastStream application instance to configure
    
    Example:
        ```python
        app = FastStream(broker=broker)
        setup_di_faststream(app)
        ```
    
    Note:
        This function should be called before starting the FastStream application
        to ensure all dependencies are properly configured.
    """
    setup_dishka_faststream(container=faststream_container(), app=app)


def setup_di_fastapi(app: FastAPI) -> None:
    """
    Configures dependency injection for a FastAPI application.
    
    Args:
        app (FastAPI): The FastAPI application instance to configure
    
    Example:
        ```python
               app = FastAPI()
        setup_di_fastapi(app)
        ```
    
    Note:
        This function should be called during application startup to ensure
        all dependencies are properly configured before handling any requests.
    """
    setup_dishka_fastapi(container=fastapi_container(), app=app)
