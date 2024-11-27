from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from faststream import FastStream
from faststream.rabbit.annotations import RabbitBroker as Broker

from app.infrastructure.message_broker.config import RabbitConfig
from app.infrastructure.message_broker.main import get_rabbit_broker
from app.main.dependency_injection.main import setup_di_fastapi, setup_di_faststream
from app.presentation.main import setup_amqp_controllers, setup_http_controllers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[FastStream, None]:
    app: FastStream = faststream_app_factory()
    await app.broker.start()
    yield
    await app.broker.close()

def faststream_app_factory() -> FastStream:
    config: RabbitConfig = RabbitConfig()
    broker: Broker = get_rabbit_broker(config=config)
    app: FastStream = FastStream(broker=broker)
    setup_amqp_controllers(broker=broker)
    setup_di_faststream(app)
    return app

def fastapi_app_factory() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    setup_http_controllers(app=app)
    setup_di_fastapi(app)
    return app
