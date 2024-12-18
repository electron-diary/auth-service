from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.entrypoint.di.providers.broker import NatsBrokerProvider
from app.entrypoint.di.providers.database import PostgresDatabaseProvider
from app.entrypoint.di.providers.handlers import HandlersProvider


def setup_container() -> AsyncContainer:
    return make_async_container(
        PostgresDatabaseProvider(),
        HandlersProvider(),
        NatsBrokerProvider(),
    )


def setup_di(app: FastAPI) -> None:
    setup_dishka(setup_container(), app)
