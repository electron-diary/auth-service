from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from faststream import FastStream
from faststream.rabbit.annotations import RabbitBroker as FastStreamRabbitBroker

from app.entrypoint.dependency_injection.main import setup_di_fastapi, setup_di_faststream
from app.infrastructure.tasks.broker import get_rabbit_broker
from app.infrastructure.tasks.config import RabbitConfig
from app.infrastructure.tasks.workers import router
from app.presentation.api.main import setup_controllers_fastapi


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    app: FastStream = setup_tasks_app()
    await app.broker.start()
    yield
    await app.broker.close()


def setup_tasks_app() -> FastStream:
    config: RabbitConfig = RabbitConfig()
    broker: FastStreamRabbitBroker = get_rabbit_broker(config=config)
    app: FastStream = FastStream(broker=broker)
    setup_di_faststream(app)
    broker.include_router(router=router)
    return app


def app_factory() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    setup_di_fastapi(app)
    setup_controllers_fastapi(app)
    return app
