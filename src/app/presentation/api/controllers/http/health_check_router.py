from dataclasses import dataclass
from fastapi import APIRouter, status

router: APIRouter = APIRouter(prefix='/healthcheck', tags=['Healthcheck'])

@dataclass(frozen=True)
class HealthcheckResponse:
    status: str = 'healthy'

@router.get('/', status_code=status.HTTP_200_OK, response_model=HealthcheckResponse)
async def healthcheck():
    return HealthcheckResponse()