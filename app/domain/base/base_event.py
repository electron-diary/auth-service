from dataclasses import dataclass, fields, asdict
from abc import ABC
from typing import Any, Self
from json import dumps
from uuid import UUID
from datetime import datetime


@dataclass(frozen=True)
class BaseDomainEvent(ABC):
    uuid: UUID
                