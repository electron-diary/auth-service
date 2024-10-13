from fastapi import FastAPI
from faststream import FastStream
from faststream.nats.annotations import NatsBroker
from dishka import FromDishka
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from src.app.infrastructure.dependency_injection.main import init_di_fastapi, init_di_faststream
from src.app.presentation.main import nats_controllers_factory, http_controllers_factory

@asynccontextmanager
async def lifespan(app: FastAPI | FastStream) -> AsyncGenerator[None, None]:
    yield


def fastapi_app_factory() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    init_di_fastapi(app = app)
    http_controllers_factory(app = app)
    return app


def faststream_app_factory() -> FastStream:
    broker: NatsBroker = FromDishka[NatsBroker]
    app: FastStream = FastStream(lifespan=lifespan)
    init_di_faststream(app = app)
    nats_controllers_factory(broker = broker)
    return app