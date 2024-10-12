from dataclasses import dataclass
from faststream.nats.router import NatsRouter


router: NatsRouter = NatsRouter(prefix="")


@dataclass(frozen=True)
class HealthcheckResponse:
    status: str = 'healthy'


@router.subscriber(stream='/health-check')
async def create_user() -> HealthcheckResponse:
    return HealthcheckResponse()