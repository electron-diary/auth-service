from dataclasses import dataclass
from typing import Any

from src.app.presentation.api.responses.base_response import BaseResponse

@dataclass(frozen=True)
class SuccessfullResponse(BaseResponse):
    status_code: int = 200
    data: Any | None = None

