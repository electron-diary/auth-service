from typing import Self, Protocol
from abc import abstractmethod


class Metrics(Protocol):
    @abstractmethod
    def add_metric(
        self: Self, metric_name: str, metric_description: str
    ) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )