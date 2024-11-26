from faststream.rabbit.annotations import RabbitBroker
from fastapi import FastAPI

from app.presentation.api.controllers import amqp
from app.presentation.api.controllers import http


def setup_http_controllers(app: FastAPI) -> None:
    app.include_router(http.router)

def setup_amqp_controllers(broker: RabbitBroker) -> None:
    broker.include_router(amqp.router)