from dataclasses import dataclass, field


@dataclass(frozen=True)
class Response:
    status: int


@dataclass(frozen=True)
class SuccessfulResponse[Result](Response):
    result: Result | None = None


@dataclass(frozen=True)
class ErrorData[Error]:
    message: str = "Error occurred"
    data: Error | None = None


@dataclass(frozen=True)
class ErrorResponse[Error](Response):
    error: ErrorData[Error] = field(default_factory=ErrorData)
