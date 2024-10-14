from typing import Protocol, Self


class Interactor[Request, Response](Protocol):
    async def __call__(self: Self, request: Request) -> Response:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )