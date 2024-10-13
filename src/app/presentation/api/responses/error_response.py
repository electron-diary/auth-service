from dataclasses import dataclass
from typing import Any

from src.app.presentation.api.responses.base_response import BaseResponse

@dataclass(frozen=True)
class ErorrResponse(BaseResponse):
    status_code: int = 500
    eror: Any | None = None

