from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.entrypoint.di.main import setup_di
from app.presentation.api.controllers.exceptions import setup_exception_handlers
from app.presentation.api.controllers.main import setup_controllers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield


def app_factory() -> FastAPI:
    app = FastAPI()
    setup_controllers(app)
    setup_di(app)
    setup_exception_handlers(app)
    return app
