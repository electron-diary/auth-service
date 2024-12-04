from app.application.base.base_mediator import MediatorInterface
from app.application.user.command_handlers.create_user import CreateUserCommandHandler
from app.application.user.command_handlers.delete_user import DeleteUserCommandHandler
from app.application.user.command_handlers.restore_user import RestoreUserCommandHandler
from app.application.user.command_handlers.update_contacts import UpdateContactsCommandHandler
from app.application.user.command_handlers.update_username import UpdateUsernameCommandHandler
from app.application.user.commands import UpdateContactsCommand, UpdateUsernameCommand, RestoreUserCommand
from app.application.user.query_handlers.get_user_by_id import GetUserByIdQueryHandler
from app.application.user.commands import CreateUserCommand, DeleteUserCommand
from app.application.user.queries import GetUserQuery


def setup_handlers(mediator: MediatorInterface) -> None:
    """
    Configures the mediator with command and query handlers for user operations.
    Implements the Mediator pattern to decouple command/query handling from their execution.

    The function registers:
    - Command handlers for user creation, updates, deletion, and restoration
    - Query handler for retrieving user information

    Args:
        mediator: The mediator instance that will coordinate command and query handling

    Example:
        mediator = Mediator()
        setup_handlers(mediator)
        # Mediator is now configured to handle all user-related commands and queries
    """
    # Register command handlers for user creation and modification operations
    mediator.register_command_handler(CreateUserCommand, CreateUserCommandHandler)
    mediator.register_command_handler(UpdateUsernameCommand, UpdateUsernameCommandHandler)
    mediator.register_command_handler(UpdateContactsCommand, UpdateContactsCommandHandler)
    mediator.register_command_handler(RestoreUserCommand, RestoreUserCommandHandler)
    mediator.register_command_handler(DeleteUserCommand, DeleteUserCommandHandler)

    # Register query handler for user retrieval operations
    mediator.register_query_handler(GetUserQuery, GetUserByIdQueryHandler)
