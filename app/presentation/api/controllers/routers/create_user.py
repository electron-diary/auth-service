from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.commands.create_user import CreateUser, CreateUserCommand
from app.application.common.exceptions import UserAlreadyExistsError
from app.presentation.api.controllers.responses import ErrorResponse, SuccessfulResponse

router = APIRouter(prefix="/user")


@router.post(
    "/create",
    responses={
        status.HTTP_201_CREATED: {
            "model": SuccessfulResponse[UUID],
        },
        status.HTTP_409_CONFLICT: {
            "model": ErrorResponse[UserAlreadyExistsError],
        },
    },
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_user(
    command: CreateUserCommand,
    use_case: FromDishka[CreateUser],
) -> SuccessfulResponse[UUID]:
    result = await use_case.handle(command)
    return SuccessfulResponse(status.HTTP_201_CREATED, result)
