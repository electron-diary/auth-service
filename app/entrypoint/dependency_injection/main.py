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
    container: AsyncContainer = make_async_container(
        MongodbProvider(),
        LocalEventBusProvider(),
        EventHandlersProvider(),
    )
    return container


def setup_di_faststream(app: FastStream) -> None:
    setup_dishka_faststream(container=faststream_container(), app=app)


def setup_di_fastapi(app: FastAPI) -> None:
    setup_dishka_fastapi(container=fastapi_container(), app=app)
