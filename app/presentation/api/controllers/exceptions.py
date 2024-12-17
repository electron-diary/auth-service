from fastapi import FastAPI
from starlette import status
from starlette.requests import Request

from app.application.common.exceptions import ApplicationError, ProfileNotFoundError, UserAlreadyExistsError, UserNotFoundError
from app.domain.common.exception import DomainError
from app.domain.profile.exceptions import AddressNotFoundError, ProfileInactiveError, SocialNetwProfileNotFoundError
from app.domain.user.exceptions import UserInactiveError
from app.presentation.api.controllers.responses import ErrorData, ErrorResponse


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ProfileNotFoundError, application_exception_handler(status=status.HTTP_404_NOT_FOUND))
    app.add_exception_handler(UserAlreadyExistsError, application_exception_handler(status=status.HTTP_409_CONFLICT))
    app.add_exception_handler(UserNotFoundError, application_exception_handler(status=status.HTTP_404_NOT_FOUND))
    app.add_exception_handler(SocialNetwProfileNotFoundError, application_exception_handler(status=status.HTTP_404_NOT_FOUND))
    app.add_exception_handler(AddressNotFoundError, application_exception_handler(status=status.HTTP_404_NOT_FOUND))
    app.add_exception_handler(ProfileInactiveError, application_exception_handler(status=status.HTTP_400_BAD_REQUEST))
    app.add_exception_handler(UserInactiveError, application_exception_handler(status=status.HTTP_400_BAD_REQUEST))
    app.add_exception_handler(Exception, unknown_exception_handler(status=status.HTTP_500_INTERNAL_SERVER_ERROR))


async def domain_exception_handler(request: Request, exception: DomainError, status: int) -> ErrorResponse:
    return ErrorResponse(
        status=status,
        message=ErrorData(data=exception.message),
    )


async def application_exception_handler(request: Request, exception: ApplicationError, status: int) -> ErrorResponse:
    return ErrorResponse(
        status=status,
        message=ErrorData(data=exception.message),
    )


async def unknown_exception_handler(request: Request, exception: Exception, status: int) -> ErrorResponse:
    return ErrorResponse(
        status=status,
        message=ErrorData(data=str(exception)),
    )
