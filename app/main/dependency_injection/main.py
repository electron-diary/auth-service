from dishka.async_container import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka as setup_dishka_fastapi
from dishka.integrations.faststream import setup_dishka as setup_dishka_faststream
from fastapi import FastAPI
from faststream import FastStream



def make_container_fastapi() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        ...
    )
    return container

def make_container_faststream() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        ...
    )
    return container

def setup_di_fastapi(app: FastAPI) -> None:
    setup_dishka_fastapi(app=app, container=make_container_fastapi())

def setup_di_faststream(app: FastStream) -> None:
    setup_dishka_faststream(app=app, container=make_container_faststream())
