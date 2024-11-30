from dataclasses import dataclass, field


@dataclass(frozen=True)
class ErrorResponse[Exc]:
    """Base error response model for API errors"""

    status: int = field(default=500)
    data: Exc = field(default=Exc)
