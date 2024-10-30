from dataclasses import dataclass
from fastapi import APIRouter, status
import logging


router: APIRouter = APIRouter(prefix='/healthcheck', tags=['Healthcheck'])

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class HealthcheckResponse:
    status: str = 'healthy'


@router.get('/', status_code=status.HTTP_200_OK, response_model=HealthcheckResponse)
async def healthcheck() -> HealthcheckResponse:
    logging.info(msg='user-service is healthy')
    return HealthcheckResponse()