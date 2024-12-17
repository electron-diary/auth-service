from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.commands.change_bio import ChangeBio, ChangeBioCommand
from app.application.common.exceptions import ProfileNotFoundError, UserNotFoundError
from app.domain.profile.exceptions import ProfileInactiveError
from app.domain.user.exceptions import UserInactiveError
from app.presentation.api.controllers.responses import ErrorResponse, SuccessfulResponse

router = APIRouter()


@router.post(
    "/change-bio",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessfulResponse,
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse[UserInactiveError | ProfileInactiveError],
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse[UserNotFoundError | ProfileNotFoundError],
        },
    },
    status_code=status.HTTP_200_OK,
)
@inject
async def change_bio(
    command: ChangeBioCommand,
    use_case: FromDishka[ChangeBio],
) -> SuccessfulResponse:
    await use_case.handle(command)
    return SuccessfulResponse(status.HTTP_200_OK)
