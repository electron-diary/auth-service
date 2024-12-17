from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.commands.delete_address import DeleteAddress, DeleteAddressCommand
from app.application.common.exceptions import UserNotFoundError
from app.domain.profile.exceptions import AddressNotFoundError
from app.domain.user.exceptions import UserInactiveError
from app.presentation.api.controllers.responses import ErrorResponse, SuccessfulResponse

router = APIRouter(prefix="/profile")


@router.delete(
    "/delete-address",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessfulResponse,
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorResponse[UserInactiveError],
        },
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorResponse[UserNotFoundError | AddressNotFoundError],
        },
    },
    status_code=status.HTTP_200_OK,
)
@inject
async def delete_address(
    command: DeleteAddressCommand,
    use_case: FromDishka[DeleteAddress],
) -> SuccessfulResponse:
    await use_case.handle(command)
    return SuccessfulResponse(status.HTTP_200_OK)
