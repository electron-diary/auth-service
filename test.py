from uuid import uuid4
import asyncio

from app.adapters.database.mongo.config import MongoConfig
from app.adapters.database.mongo.event_storage_collection import get_collection
from app.adapters.database.mongo.main import mongo_client, mongo_session
from app.adapters.database.mongo.event_storage_database import get_database
from app.adapters.database.mongo.event_storage_repository import EventSoreRepository
from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.domain.value_objects.uuid_value_object import UUIDValueObject
from app.domain.entities.user_entity import UserDomainEntity

# config = MongoConfig(
#     host='localhost',
#     port=27017,
#     username='root',
#     password='example',
#     database='event-sourcing',
#     collection='MongoEvents'
# )

# client = mongo_client(config=config)
# db = get_database(mongo_client=client, config=config)
# collection = get_collection(database=db, config=config)
# uuid = uuid4()


# async def get_repository() -> EventSoreRepository:
#     session = await mongo_session(client=client)
#     return EventSoreRepository(
#         session=session,
#         collection=collection
#     )

# event = DeleteUserEvent(
#     uuid=uuid
# )








