from dataclasses import dataclass

from src.app.presentation.api.responses.base_response import BaseResponse

@dataclass(frozen=True)
class ErorrResponse[ErorType](BaseResponse):
    status_code: int = 500
    eror: ErorType | None = None

