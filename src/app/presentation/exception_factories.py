from fastapi import status, FastAPI
from faststream.nats.annotations import NatsBroker
from faststream import ExceptionMiddleware

from src.app.domain.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from src.app.domain.common.exceptions import DomainValidationError
from src.app.presentation.exception_handlers import user_already_exists_exception_handler, user_not_found_exception_handler
from src.app.presentation.exception_handlers import domain_validation_exception_handler, internal_server_error_exception_handler
from src.app.presentation.exception_handlers import faststream_domain_validation_exception_handler, faststream_internal_server_error_exception_handler
from src.app.presentation.exception_handlers import faststream_user_already_exists_exception_handler, faststream_user_not_found_exception_handler


def fastapi_exceptions_factory(app: FastAPI) -> None:
    app.add_exception_handler(UserAlreadyExistsError, user_already_exists_exception_handler)
    app.add_exception_handler(UserNotFoundError, user_not_found_exception_handler)
    app.add_exception_handler(DomainValidationError, domain_validation_exception_handler)
    app.add_exception_handler(Exception, internal_server_error_exception_handler)



def nats_exceptions_factory(broker: NatsBroker) -> None:
    exc_middleware: ExceptionMiddleware = ExceptionMiddleware(
        publish_handlers={
            UserAlreadyExistsError: faststream_user_already_exists_exception_handler,
            UserNotFoundError: faststream_user_not_found_exception_handler,
            DomainValidationError: faststream_domain_validation_exception_handler,
            Exception: faststream_internal_server_error_exception_handler
        }
    )
    broker.add_middleware(middleware=exc_middleware)
        