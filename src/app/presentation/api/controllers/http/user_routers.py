from typing import Annotated
from fastapi import APIRouter, status
from dishka.integrations.fastapi import inject, FromDishka

from src.app.application.dto.request_dto import CreateUserRequest, GetUserRequest, UpdateUserContactRequest
from src.app.application.dto.request_dto import UpdateUserNameRequest, DeleteUserRequest
from src.app.application.dto.response_dto import CreateUserResponse, GetUserResponse
from src.app.application.dto.response_dto import UpdateUserContactResponse, UpdateUserNameResponse
from src.app.application.interfaces.interactor import Interactor
from src.app.application.usecases.create_user_usecase import CreateUserUseCase
from src.app.application.usecases.get_user_usecase import GetUserUseCase
from src.app.application.usecases.update_user_contact_usecase import UpdateUserContactUseCase
from src.app.application.usecases.update_user_name_usecase import UpdateUserNameUseCase
from src.app.application.usecases.delete_user_usecase import DeleteUserUseCase


router: APIRouter = APIRouter(prefix='/users', tags=['Users'])


@router.post(
    '/create-user', status_code=status.HTTP_201_CREATED, response_model= CreateUserResponse
)
@inject
async def create_user(
    user_shema: CreateUserRequest, interactor: Annotated[Interactor, FromDishka[CreateUserUseCase]]
) -> CreateUserResponse:
    return await interactor(
        request=user_shema
    )


@router.get(
    '/get-user', status_code=status.HTTP_200_OK, response_model=GetUserResponse
)
@inject
async def get_user(
    user_shema: GetUserRequest, interactor: Annotated[Interactor, FromDishka[GetUserUseCase]]
) -> GetUserResponse:
    return await interactor(
        request=user_shema
    )


@router.put(
    '/update-user-contact', status_code=status.HTTP_200_OK, response_model=UpdateUserContactResponse
)
@inject
async def update_user_contact(
    user_shema: UpdateUserContactRequest, interactor: Annotated[Interactor, FromDishka[UpdateUserContactUseCase]]
) -> UpdateUserContactResponse:
    return await interactor(
        request=user_shema
    )


@router.put(
    '/update-user-name', status_code=status.HTTP_200_OK, response_model=UpdateUserNameResponse
)
@inject
async def update_user_name(
    user_shema: UpdateUserNameRequest, interactor: Annotated[Interactor, FromDishka[UpdateUserNameUseCase]]
) -> UpdateUserNameResponse:
    return await interactor(
        request=user_shema
    )


@router.delete(
    '/delete-user', status_code=status.HTTP_200_OK
)
@inject
async def delete_user(
    user_shema: DeleteUserRequest, interactor: Annotated[Interactor, FromDishka[DeleteUserUseCase]]
) -> None:
    return await interactor(
        request=user_shema
    )


