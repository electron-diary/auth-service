from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.commands.add_social_netw_profile import AddSocialNetwProfile, AddSocialNetwProfileCommand
from app.application.common.exceptions import ProfileNotFoundError, UserNotFoundError
from app.domain.profile.exceptions import ProfileInactiveError
from app.domain.user.exceptions import UserInactiveError
from app.presentation.api.controllers.responses import ErrorResponse, SuccessfulResponse

router = APIRouter(prefix="/profile")


@router.post(
    "/add-social-netw-profile",
    responses={
        status.HTTP_201_CREATED: {
            "model": SuccessfulResponse,
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse[UserInactiveError | ProfileInactiveError],
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse[UserNotFoundError | ProfileNotFoundError],
        },
    },
    status_code=status.HTTP_201_CREATED,
)
@inject
async def add_social_netw_profile(
    command: AddSocialNetwProfileCommand,
    use_case: FromDishka[AddSocialNetwProfile],
) -> SuccessfulResponse:
    await use_case.handle(command)
    return SuccessfulResponse(status.HTTP_201_CREATED)
