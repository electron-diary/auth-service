from fastapi import FastAPI
from faststream import FastStream
from dishka.integrations.fastapi import setup_dishka as setup_dishka_fastapi
from dishka.integrations.faststream import setup_dishka as setup_dishka_faststream

from app.main.dependency_injection.factories import container_factory


def init_di_fastapi(app: FastAPI) -> None:
    setup_dishka_fastapi(container = container_factory(), app = app)


def init_di_faststream(app: FastStream) -> None:
    setup_dishka_faststream(container = container_factory(), app = app)