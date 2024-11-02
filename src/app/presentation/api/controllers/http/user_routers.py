from uuid import UUID
from fastapi import APIRouter, status
from dishka.integrations.fastapi import inject, FromDishka

from app.application.dto.request_dto import CreateUserRequest, GetUserRequest, UpdateUserContactRequest, EditUserStatusRequest
from app.application.dto.request_dto import UpdateUserNameRequest, DeleteUserRequest
from app.application.dto.response_dto import CreateUserResponse, GetUserResponse
from app.application.dto.response_dto import UpdateUserContactResponse, UpdateUserNameResponse
from app.application.usecases.create_user_usecase import CreateUserUseCase
from app.application.usecases.get_user_usecase import GetUserUseCase
from app.application.usecases.update_user_contact_usecase import UpdateUserContactUseCase
from app.application.usecases.update_user_name_usecase import UpdateUserNameUseCase
from app.application.usecases.delete_user_usecase import DeleteUserUseCase
from app.application.usecases.edit_user_status import EditUserStatusUseCase
from app.infrastructure.metrics.decorators import measure_time


router: APIRouter = APIRouter(prefix='/users', tags=['Users'])


@router.post(
    '/create-user', status_code=status.HTTP_201_CREATED, response_model= CreateUserResponse
)
@inject
@measure_time
async def create_user(
    user_shema: CreateUserRequest, interactor: FromDishka[CreateUserUseCase]
) -> CreateUserResponse:
    return await interactor(request=user_shema)


@router.get(
    '/get-user', status_code=status.HTTP_200_OK, response_model=GetUserResponse
)
@inject
@measure_time
async def get_user(
    user_uuid: UUID, interactor: FromDishka[GetUserUseCase]
) -> GetUserResponse:
    return await interactor(request=GetUserRequest(user_uuid=user_uuid))


@router.put(
    '/update-user-contact', status_code=status.HTTP_200_OK, response_model=UpdateUserContactResponse
)
@inject
@measure_time
async def update_user_contact(
    user_shema: UpdateUserContactRequest, interactor: FromDishka[UpdateUserContactUseCase]
) -> UpdateUserContactResponse:
    return await interactor(request=user_shema)


@router.put(
    '/update-user-name', status_code=status.HTTP_200_OK, response_model=UpdateUserNameResponse
)
@inject
@measure_time
async def update_user_name(
    user_shema: UpdateUserNameRequest, interactor: FromDishka[UpdateUserNameUseCase]
) -> UpdateUserNameResponse:
    return await interactor(request=user_shema)


@router.delete(
    '/delete-user', status_code=status.HTTP_200_OK
)
@inject
@measure_time
async def delete_user(
    user_shema: DeleteUserRequest, interactor: FromDishka[DeleteUserUseCase]
) -> None:
    return await interactor(request=user_shema)


@router.post(
    '/edit-user-status', status_code=status.HTTP_200_OK, response_model=None
)
@inject
@measure_time
async def edit_user_status(
    user_shema: EditUserStatusRequest, interactor: FromDishka[EditUserStatusUseCase]
) -> None:
    return await interactor(request=user_shema)
