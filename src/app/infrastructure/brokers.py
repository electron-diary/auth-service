from faststream.nats import NatsBroker
from faststream.security import SASLPlaintext


def nats_broker(config: ...) -> NatsBroker:
    broker: NatsBroker = NatsBroker(
        servers=config.NATS_URL,
        user=config.NATS_USERNAME,
        password=config.NATS_PASSWORD
    )
    return broker
