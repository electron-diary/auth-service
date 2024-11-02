from dataclasses import dataclass
from faststream.nats.router import NatsRouter

from app.infrastructure.metrics.decorators import measure_time


router: NatsRouter = NatsRouter(prefix='/healthcheck')


@dataclass(frozen=True)
class HealthcheckResponse:
    status: str = 'healthy'


@router.subscriber('/health-check')
@measure_time
async def create_user() -> HealthcheckResponse:
    return HealthcheckResponse()