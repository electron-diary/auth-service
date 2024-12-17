from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.dto.user_dto import UserDto
from app.application.queries.get_user_by_id import GetUserById, GetUserByIdQuery
from app.presentation.api.controllers.responses import SuccessfulResponse

router = APIRouter()


@router.get(
    "/{user_id}",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessfulResponse[UserDto | None],
        },
    },
    status_code=status.HTTP_200_OK,
)
@inject
async def get_profile_by_id(
    user_id: UUID,
    use_case: FromDishka[GetUserById],
) -> SuccessfulResponse[UserDto | None]:
    query = GetUserByIdQuery(user_id)
    user = await use_case.handle(query)
    return SuccessfulResponse(status.HTTP_200_OK, user)
