from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.commands.delete_social_netw_profile import DeleteSocialNetwProfile, DeleteSocialNetwProfileCommand
from app.application.common.exceptions import ProfileNotFoundError, UserNotFoundError
from app.domain.profile.exceptions import ProfileInactiveError, SocialNetwProfileNotFoundError
from app.domain.user.exceptions import UserInactiveError
from app.presentation.api.controllers.responses import ErrorResponse, SuccessfulResponse

router = APIRouter()


@router.delete(
    "/delete-social-netw-profile",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessfulResponse,
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse[UserInactiveError | ProfileInactiveError],
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse[
                UserNotFoundError | ProfileNotFoundError | SocialNetwProfileNotFoundError
            ],
        },
    },
    status_code=status.HTTP_200_OK,
)
@inject
async def delete_social_netw_profile(
    use_case: FromDishka[DeleteSocialNetwProfile],
    command: DeleteSocialNetwProfileCommand,
)->SuccessfulResponse:
    await use_case.handle(command)
    return SuccessfulResponse(status.HTTP_200_OK)
