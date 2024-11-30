from fastapi import FastAPI

from app.presentation.api.controllers.user import router
from app.presentation.api.controllers.metrics import metrics


def setup_controllers_fastapi(app: FastAPI) -> None:
    app.include_router(router)
    app.include_router(metrics)
