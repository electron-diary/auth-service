from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.dto.profile_dto import ProfileDto
from app.application.queries.get_user_profiles import GetUserProfiles, GetUserProfilesQuery
from app.presentation.api.controllers.responses import SuccessfulResponse

router = APIRouter(prefix="/profile")


@router.get(
    "/profiles/{profile_owner_id}",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessfulResponse[list[ProfileDto]],
        },
    },
    status_code=status.HTTP_200_OK,
)
@inject
async def get_profile_by_id(
    profile_owner_id: UUID,
    use_case: FromDishka[GetUserProfiles],
) -> SuccessfulResponse[list[ProfileDto]]:
    query = GetUserProfilesQuery(profile_owner_id)
    profiles = await use_case.handle(query)
    return SuccessfulResponse(status.HTTP_200_OK, profiles)
