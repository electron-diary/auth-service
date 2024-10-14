from fastapi import Request, status, responses
from typing import cast

from src.app.presentation.api.responses.error_response import ErorrResponse
from src.app.domain.exceptions.user_exceptions import UserAlreadyExistsError, UserNotFoundError
from src.app.domain.common.exceptions import DomainValidationError


async def user_already_exists_exception_handler(
    request: Request | None , exc: UserAlreadyExistsError
) -> responses.JSONResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message}
    )

async def user_not_found_exception_handler(
    request: Request | None, exc: UserNotFoundError
) -> responses.JSONResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message}
    )

async def domain_validation_exception_handler(
    request: Request | None, exc: DomainValidationError) -> responses.JSONResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": cast(str, exc.message)}
    )

async def internal_server_error_exception_handler(
    request: Request | None, exc: Exception
) -> responses.JSONResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal Server Error"}
    )



async def faststream_user_already_exists_exception_handler(exc: UserAlreadyExistsError) -> ErorrResponse:
    return ErorrResponse(
        status_code=status.HTTP_409_CONFLICT,
        eror={"message": exc.message}
    )

async def faststream_user_not_found_exception_handler(exc: UserNotFoundError) -> ErorrResponse:
    return ErorrResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        eror={"message": exc.message}
    )

async def faststream_domain_validation_exception_handler(exc: DomainValidationError) -> ErorrResponse:
    return ErorrResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        eror={"message": cast(str, exc.message)}
    )

async def faststream_internal_server_error_exception_handler(exc: Exception) -> ErorrResponse:
    return ErorrResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        eror={"message": "Internal Server Error"}
    )




