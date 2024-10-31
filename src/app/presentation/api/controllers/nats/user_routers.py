from faststream.nats.router import NatsRouter
from dishka.integrations.faststream import inject, FromDishka

from app.application.dto.request_dto import CreateUserRequest, GetUserRequest, UpdateUserContactRequest
from app.application.dto.request_dto import UpdateUserNameRequest, DeleteUserRequest
from app.application.dto.response_dto import CreateUserResponse, GetUserResponse
from app.application.dto.response_dto import UpdateUserContactResponse, UpdateUserNameResponse
from app.application.usecases.create_user_usecase import CreateUserUseCase
from app.application.usecases.get_user_usecase import GetUserUseCase
from app.presentation.api.responses.successful_response import SuccessfullResponse
from app.application.usecases.update_user_contact_usecase import UpdateUserContactUseCase
from app.application.usecases.update_user_name_usecase import UpdateUserNameUseCase
from app.application.usecases.delete_user_usecase import DeleteUserUseCase


router: NatsRouter = NatsRouter(prefix='/users')


@router.subscriber('/create-user')
@inject
async def create_user(
    user_shema: CreateUserRequest, interactor: FromDishka[CreateUserUseCase]
) -> CreateUserResponse:
    response: CreateUserResponse = await interactor(request=user_shema)
    return SuccessfullResponse(data=response)


@router.subscriber('/get-user')
@inject
async def get_user(
    user_shema: GetUserRequest, interactor: FromDishka[GetUserUseCase]
) -> GetUserResponse:
    response: GetUserResponse = await interactor(request=user_shema)
    return SuccessfullResponse(data=response)


@router.subscriber('/update-user-contact')
@inject
async def update_user_contact(
    user_shema: UpdateUserContactRequest, interactor: FromDishka[UpdateUserContactUseCase]
) -> UpdateUserContactResponse:
    response: UpdateUserContactResponse = await interactor(request=user_shema)
    return SuccessfullResponse(data=response)


@router.subscriber('/update-user-name')
@inject
async def update_user_name(
    user_shema: UpdateUserNameRequest, interactor: FromDishka[UpdateUserNameUseCase]
) -> UpdateUserNameResponse:
    response: UpdateUserNameResponse = await interactor(request=user_shema)
    return SuccessfullResponse(data=response)


@router.subscriber('/delete-user')
@inject
async def delete_user(
    user_shema: DeleteUserRequest, interactor: FromDishka[DeleteUserUseCase]
) -> None:
    await interactor(request=user_shema)