from dataclasses import dataclass
from fastapi import APIRouter, status
import logging

from app.infrastructure.metrics.decorators import measure_time

router: APIRouter = APIRouter(prefix='/healthcheck', tags=['Healthcheck'])

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class HealthcheckResponse:
    status: str = 'healthy'


@router.get('/', status_code=status.HTTP_200_OK, response_model=HealthcheckResponse)
@measure_time
async def healthcheck() -> HealthcheckResponse:
    logging.info(msg='user-service is healthy')
    return HealthcheckResponse()