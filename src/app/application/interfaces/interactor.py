from typing import Protocol, Self


class Interactor[Reuqest, Response](Protocol):
    async def __call__(self: Self, request: Reuqest) -> Response:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )