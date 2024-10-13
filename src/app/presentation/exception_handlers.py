from fastapi import Request, status, responses
from typing import cast

from src.app.presentation.api.responses.error_response import ErorrResponse
from src.app.domain.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from src.app.domain.common.exceptions import DomainValidationError


async def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsError) -> ErorrResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": exc.message}
    )

async def user_not_found_exception_handler(request: Request, exc: UserNotFoundError) -> ErorrResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exc.message}
    )

async def domain_validation_exception_handler(request: Request, exc: DomainValidationError) -> ErorrResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": cast(str, exc.message)}
    )

async def internal_server_error_exception_handler(request: Request, exc: Exception) -> ErorrResponse:
    return responses.JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal Server Error"}
    )


