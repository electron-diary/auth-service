from faststream.asgi import AsgiFastStream
from faststream import Logger
from faststream.nats import NatsBroker
import asyncio

broker = NatsBroker('nats://localhost:4222')
app = AsgiFastStream(broker)

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetUserRequest:
    user_uuid: UUID


@dataclass(frozen=True)
class CreateUserRequest:
    user_name: str
    user_contact: str | int


@dataclass(frozen=True)
class DeleteUserRequest:
    user_uuid: UUID


@dataclass(frozen=True)
class UpdateUserContactRequest:
    user_uuid: UUID
    user_contact: str | int


@dataclass(frozen=True)
class UpdateUserNameRequest:
    user_uuid: UUID
    user_name: str

async def publish_create_user():
    msg = await broker.publish(
        message=CreateUserRequest(user_name='test', user_contact='test'), subject='/users/create-user ', rpc=True
    )
    print(msg)


@app.after_startup
async def run_messages():
    await publish_create_user()