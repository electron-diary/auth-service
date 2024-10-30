from fastapi import FastAPI
from faststream.asgi import AsgiFastStream
from faststream.nats.annotations import NatsBroker
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from src.app.main.dependency_injection.main import init_di_fastapi, init_di_faststream
from src.app.presentation.main import nats_controllers_factory, http_controllers_factory
from src.app.infrastructure.brokers.factories import BrokerFactory
from src.app.main.config_loader import load_nats_config
from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.logger.main import configure_logging

@asynccontextmanager
async def lifespan(app: FastAPI | AsgiFastStream) -> AsyncGenerator[None, None]:
    configure_logging()
    yield


def fastapi_app_factory() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    init_di_fastapi(app = app)
    http_controllers_factory(app = app)
    return app


def faststream_app_factory() -> AsgiFastStream:
    config: NatsConfig = load_nats_config()
    broker_factory: BrokerFactory = BrokerFactory(config = config)
    broker: NatsBroker = broker_factory.get_broker()
    app: AsgiFastStream = AsgiFastStream(broker, asyncapi_path='/docs')
    init_di_faststream(app = app)
    nats_controllers_factory(broker = broker)
    return app