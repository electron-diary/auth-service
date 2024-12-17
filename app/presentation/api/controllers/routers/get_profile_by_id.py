from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.dto.profile_dto import ProfileDto
from app.application.queries.get_profile_by_id import GetProfileById, GetProfileByIdQuery
from app.presentation.api.controllers.responses import SuccessfulResponse

router = APIRouter()


@router.get(
    "/{profile_id}",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessfulResponse[ProfileDto | None],
        },
    },
    status_code=status.HTTP_200_OK,
)
@inject
async def get_profile_by_id(
    profile_id: UUID,
    use_case: FromDishka[GetProfileById],
) -> SuccessfulResponse[ProfileDto | None]:
    query = GetProfileByIdQuery(profile_id)
    profile = await use_case.handle(query)
    return SuccessfulResponse(status.HTTP_200_OK, profile)
