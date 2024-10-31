from fastapi import APIRouter
from starlette import status
from dishka.integrations.fastapi import inject, FromDishka

from app.application.dto.response_dto import AuthentificationResponse
from app.application.dto.request_dto import AuthentificateUserRequest
from app.application.usecases.authentificate_user import AuthentificateUserUseCase

router: APIRouter = APIRouter(prefix='/users/authentification', tags=['Authentification'])


@router.post(
    '/authentificate', response_model=AuthentificationResponse, status_code=status.HTTP_201_CREATED
)
@inject
async def authentificate_user(
    user_shema: AuthentificateUserRequest, interactor: FromDishka[AuthentificateUserUseCase]
) -> AuthentificationResponse:
    return await interactor(request=user_shema)