from dataclasses import dataclass


@dataclass(eq=False)
class DomainError(Exception):
    message: str
