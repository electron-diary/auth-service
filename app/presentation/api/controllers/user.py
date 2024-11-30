from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter
from starlette import status

from app.application.user.command_handlers import (
    CreateUserCommandHandler,
    DeleteUserCommandHandler,
    RestoreUserCommandHandler,
    UpdateContactsCommandHandler,
    UpdateUsernameCommandHandler,
)
from app.application.user.commands import (
    CreateUserCommand,
    DeleteUserCommand,
    RestoreUserCommand,
    UpdateContactsCommand,
    UpdateUsernameCommand,
)
from app.application.user.query_handlers import GetUserByIdQueryHandler
from app.application.user.dtos import UserDTO
from app.application.user.queries import GetUserQuery
from app.application.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from app.domain.user.exceptions import UserException
from app.presentation.api.responses.error_response import ErrorResponse


router: APIRouter = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "/create",
    response_model=UserDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "User successfully created",
            "model": UserDTO
        },
        status.HTTP_409_CONFLICT: {
            "description": "User already exists",
            "content": {
                "application/json": {
                    "example": {"detail": "User with this phone number already exists"}
                }
            },
            'model': ErrorResponse
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad request",
            "content": {
                "application/json": {
                    "example": {"detail": "Bad request"}
                }
            },
            'model': ErrorResponse
        }
    }
)
@inject
async def create_user(
    command: CreateUserCommand, handler: FromDishka[CreateUserCommandHandler],
) -> UUID:
    """
    Create a new user with the provided details.
    
    Args:
        command: User creation command containing user details
        handler: Injected command handler
    
    Returns:
        Created user UUID
    
    Raises:
        UserAlreadyExistsError: If user with provided details already exists
    """
    return await handler(command=command)


@router.put(
    "/update_username", 
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "Username successfully updated",
            "content": {
                "application/json": {
                    "example": {"message": "Username updated successfully"}
                }
            },
            "model": None
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid username format",
            "content": {
                "application/json": {
                    "example": {"detail": "Username must be between 3 and 30 characters"}
                }
            }, 
            "model": ErrorResponse
            
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {"detail": "User with specified ID not found"}
                }
            },
            "model": ErrorResponse
        },
    }

)
@inject
async def update_username(
    command: UpdateUsernameCommand, handler: FromDishka[UpdateUsernameCommandHandler],
) -> None:
    """
    Update the username for an existing user.

    Args:
        command (UpdateUsernameCommand): Command containing user ID and new username
        handler (UpdateUsernameCommandHandler): Injected command handler

    Raises:
        UserNotFoundError or UserException: When user is not found or username validation fails
    """
    return await handler(command=command)


@router.put(
    "/update_contacts",
    status_code=status.HTTP_200_OK,
    responses = {
        status.HTTP_200_OK: {
            "description": "User contacts successfully updated",
            "content": {
                "application/json": {
                    "example": {"message": "User contacts updated successfully"}
                }
            },
            "model": None
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "error_code": "USER_NOT_FOUND",
                        "message": "User with specified ID does not exist"
                    }
                }
            },
            "model": ErrorResponse
        },
        status.HTTP_409_CONFLICT: {
            "description": "User already exists",
            "content": {
                "application/json": {
                    "example": {"detail": "User with this phone number already exists"}
                }
            },
            'model': ErrorResponse
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid username format",
            "content": {
                "application/json": {
                    "example": {"detail": "User phone must be int"}
                }
            }, 
            "model": ErrorResponse
        }
    }
)
@inject
async def update_contacts(
    command: UpdateContactsCommand, handler: FromDishka[UpdateContactsCommandHandler],
) -> None:
    """
    Update contact information for an existing user.

    Args:
        command: Contact update command containing user ID and new contact information
        handler (UpdateContactsCommandHandler): Injected command handler

    Raises:
        UserAlreadyExistsError or UserException: When user is exists or contact validation fails
    """
    await handler(command=command)


@router.delete(
    "/delete",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "User successfully deleted",
            "model": None,
            "content": {
                "application/json": {
                    "example": {
                        "message": "User successfully deleted",
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "message": "User with specified ID does not exist"
                    }
                }
            }
        },
        status.HTTP_409_CONFLICT: {
            "description": "Invalid request",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "message": "Invalid user ID format"
                    }
                }
            }
        },
    }
)
@inject
async def delete_user(
    command: DeleteUserCommand, handler: FromDishka[DeleteUserCommandHandler],
) -> None:
    """
    Delete a user from the system (soft delete).

    Args:
        user_id: The UUID of the user to delete
        handler: Injected command handler for user deletion

    Raises:
        UserNotFoundError or UserException: When user is not found or deletion fails
    """
    await handler(command=command)


@router.post(
    "/restore",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "description": "User successfully restored",
            "model": None,
            "content": {
                "application/json": {
                    "example": {
                        "message": "User successfully restored",
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "message": "User with specified ID does not exist"
                    }
                }
            }
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid restore operation",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "message": "User is not in deleted state"
                    }
                }
            }
        }
    },
)
@inject
async def restore_user(
    command: RestoreUserCommand, handler: FromDishka[RestoreUserCommandHandler],
) -> None:
    """
    Restore a previously deleted user.

    Args:
        handler: Injected command handler for user restoration

    Raises:
        UserException or UserNotFoundError: When user is not found or restoration fails
    """
    await handler(command=command)


@router.get(
    "/{id}",
    response_model=UserDTO,
    responses={
        status.HTTP_200_OK: {
            "description": "User details retrieved successfully",
            "model": UserDTO,
            "content": {
                "application/json": {
                    "example": {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "username": "john_doe",
                        "email": "john@example.com",
                        "created_at": "2024-01-01T00:00:00Z",
                        "updated_at": "2024-01-20T12:00:00Z",
                        "retrieved_at": "2024-01-20T12:00:00Z"
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "model": ErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "message": "User with specified ID does not exist"
                    }
                }
            }
        },
    }
)
@inject
async def get_user(
    id: UUID, handler: FromDishka[GetUserByIdQueryHandler],
) -> UserDTO:
    """
    Retrieve user details by ID with caching support.

    Args:
        id: The UUID of the user to retrieve
        handler: Injected query handler for user retrieval

    Returns:
        UserDto: User details with retrieval timestamp

    Raises:
        UserNotFoundError: When user is not found or retrieval fails
    """
    query: GetUserQuery = GetUserQuery(user_id=id)
    return await handler(query=query)

