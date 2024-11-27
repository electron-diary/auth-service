from dishka.async_container import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka as setup_dishka_fastapi
from dishka.integrations.faststream import setup_dishka as setup_dishka_faststream
from fastapi import FastAPI
from faststream import FastStream

from app.main.dependency_injection.provide_adapters import MongoProvider, RabbitProvider, SqlaProvider
from app.main.dependency_injection.provide_handlers import CommandHandlersProvider, EventHandlersProvider, QueryHandlersProvider


def make_container() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        SqlaProvider(),
        MongoProvider(),
        RabbitProvider(),
        EventHandlersProvider(),
        CommandHandlersProvider(),
        QueryHandlersProvider(),
    )
    return container

def setup_di_fastapi(app: FastAPI) -> None:
    setup_dishka_fastapi(app=app, container=make_container())

def setup_di_faststream(app: FastStream) -> None:
    setup_dishka_faststream(app=app, container=make_container())
