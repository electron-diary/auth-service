from dataclasses import dataclass

from src.app.presentation.api.responses.base_response import BaseResponse

@dataclass(frozen=True)
class SuccessfullResponse[DataType](BaseResponse):
    status_code: int = 200
    data: DataType | None = None

