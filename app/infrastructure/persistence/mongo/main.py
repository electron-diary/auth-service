from bson import UuidRepresentation
from bson.codec_options import CodecOptions
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession, AsyncIOMotorCollection, AsyncIOMotorDatabase

from app.infrastructure.persistence.mongo.config import MongoConfig


def mongo_client(config: MongoConfig) -> AsyncIOMotorClient:
    client: AsyncIOMotorClient = AsyncIOMotorClient(config.get_connection_uri)
    return client

async def mongo_session(client: AsyncIOMotorClient) -> AsyncIOMotorClientSession:
    session: AsyncIOMotorClientSession = await client.start_session()
    return session

def get_database(mongo_client: AsyncIOMotorClient, config: MongoConfig) -> AsyncIOMotorDatabase:
    database: AsyncIOMotorDatabase = AsyncIOMotorDatabase(client=mongo_client, name=config.database)
    return database

def get_collection(database: AsyncIOMotorDatabase, config: MongoConfig) -> AsyncIOMotorCollection:
    collection: AsyncIOMotorCollection = AsyncIOMotorCollection(database=database, name=config.collection)
    return collection.with_options(codec_options=CodecOptions(uuid_representation=UuidRepresentation.STANDARD))
