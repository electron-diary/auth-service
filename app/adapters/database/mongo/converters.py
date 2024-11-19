from json import dumps, loads
from dataclasses import asdict

from app.adapters.database.mongo.payloads import MongoEvent
from app.domain.base.base_event import BaseDomainEvent


def domain_event_to_json(event: BaseDomainEvent) -> bytes:
    event: dict = asdict(event)
    event["uuid"] = str(event["uuid"])
    return dumps(event).encode("utf-8")

def convert_domain_event_to_mongo_event(event: BaseDomainEvent) -> MongoEvent:
    mongo_event: MongoEvent = MongoEvent(
        uuid=str(event.uuid),
        event_json=domain_event_to_json(event),
        event_name=event.__class__.__name__,
    )
    return mongo_event

        






