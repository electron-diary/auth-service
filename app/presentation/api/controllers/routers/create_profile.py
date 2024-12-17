from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.commands.create_profile import CreateProfile, CreateProfileCommand
from app.application.common.exceptions import UserNotFoundError
from app.domain.user.exceptions import UserInactiveError
from app.presentation.api.controllers.responses import ErrorResponse, SuccessfulResponse

router = APIRouter(prefix="/profile")


@router.post(
    "/create",
    responses={
        status.HTTP_201_OK: {
            "model": SuccessfulResponse[UUID],
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse[UserInactiveError],
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse[UserNotFoundError],
        },
    },
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_profile(
    command: CreateProfileCommand,
    use_case: FromDishka[CreateProfile],
) -> SuccessfulResponse[UUID]:
    result = await use_case.handle(command)
    return SuccessfulResponse(status.HTTP_201_CREATED, result)
