from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.commands.delete_profile import DeleteProfile, DeleteProfileCommand
from app.application.common.exceptions import ProfileNotFoundError, UserNotFoundError
from app.domain.user.exceptions import UserInactiveError
from app.presentation.api.controllers.responses import ErrorResponse, SuccessfulResponse

router = APIRouter()


@router.delete(
    "/delete-profile",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessfulResponse,
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse[UserInactiveError],
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse[UserNotFoundError | ProfileNotFoundError],
        },
    },
    status_code=status.HTTP_200_OK,
)
@inject
async def delete_profile(
    command: DeleteProfileCommand,
    use_case: FromDishka[DeleteProfile],
) -> SuccessfulResponse:
    await use_case.handle(command)
    return SuccessfulResponse(status.HTTP_200_OK)
