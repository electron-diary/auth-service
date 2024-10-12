from fastapi import status, FastAPI
from faststream.nats.annotations import NatsBroker
from faststream import ExceptionMiddleware

from src.app.domain.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from src.app.domain.common.exceptions import DomainValidationError


def fastapi_exceptions_factory(app: FastAPI) -> None:
    app.add_exception_handler(UserAlreadyExistsError, status.HTTP_409_CONFLICT)
    app.add_exception_handler(UserNotFoundError, status.HTTP_404_NOT_FOUND)
    app.add_exception_handler(DomainValidationError, status.HTTP_400_BAD_REQUEST)
    app.add_exception_handler(Exception, status.HTTP_500_INTERNAL_SERVER_ERROR)


def nats_exceptions_factory(broker: NatsBroker) -> None:
    broker.add_middleware(ExceptionMiddleware(
        handlers={
            UserAlreadyExistsError: status.HTTP_409_CONFLICT,
            UserNotFoundError: status.HTTP_404_NOT_FOUND,
            DomainValidationError: status.HTTP_400_BAD_REQUEST,
            Exception: status.HTTP_500_INTERNAL_SERVER_ERROR
        }
    ))