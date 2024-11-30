from dataclasses import dataclass


@dataclass
class DomainException(Exception):
    message: str
