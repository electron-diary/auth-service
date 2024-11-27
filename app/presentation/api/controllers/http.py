from uuid import UUID
from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, inject

from app.application.user.commands import CreateUserCommand, DeleteUserCommand
from app.application.user.commands import UpdateContactsCommand, RestoreUserCommand, UpdateUsernameCommand
from app.application.user.queries import GetUserActionsQuery, GetUserByIdQuery, GetUsersQuery
from app.application.user.command_handlers import (
    CreateUserCommandHandler,
    DeleteUserCommandHandler,
    RestoreUserCommandHandler,
    UpdateContactsCommandHandler,
    UpdateUsernameCommandHandler
)
from app.application.user.query_handlers import (
    GetUserActionsQueryHandler,
    GetUserByIdQueryHandler,
    GetUsersQueryHandler,
)


router: APIRouter = APIRouter(prefix='/users', tags=['Users'])


@router.post('/create')
@inject
async def create_user(
    command: CreateUserCommand, handler: FromDishka[CreateUserCommandHandler]
) -> UUID:
    return await handler(command)

@router.post('/update/username')
@inject
async def update_username(
    command: UpdateUsernameCommand, handler: FromDishka[UpdateUsernameCommandHandler]
) -> None:
    await handler(command)

@router.post('/update/contacts')
@inject
async def update_contacts(
    command: UpdateContactsCommand, handler: FromDishka[UpdateContactsCommandHandler]
) -> None:
    await handler(command)

@router.post('/delete')
@inject
async def delete_user(
    command: DeleteUserCommand, handler: FromDishka[DeleteUserCommandHandler]
) -> None:
    await handler(command)

@router.post('/restore')
@inject
async def restore_user(
    command: RestoreUserCommand, handler: FromDishka[RestoreUserCommandHandler]
) -> None:
    await handler(command)


