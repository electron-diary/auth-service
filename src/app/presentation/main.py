from fastapi import FastAPI
from faststream.nats.annotations import NatsBroker

from src.app.presentation.api.controllers.nats import user_routers as nats_users, health_check_router as nats_health
from src.app.presentation.api.controllers.http import user_routers as http_users, health_check_router as http_health
from src.app.presentation.api.controllers.http import user_authentification as http_auth
from src.app.presentation.exception_factories import nats_exceptions_factory
from src.app.presentation.exception_factories import fastapi_exceptions_factory


def nats_controllers_factory(broker: NatsBroker) -> None:
    broker.include_router(nats_users.router)
    broker.include_router(nats_health.router)
    nats_exceptions_factory(broker = broker)
    

def http_controllers_factory(app: FastAPI) -> None:
    app.include_router(http_users.router)
    app.include_router(http_health.router)
    app.include_router(http_auth.router)
    fastapi_exceptions_factory(app = app)